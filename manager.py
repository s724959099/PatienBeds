from line_api import LineAPI
from util.commands import Invoker, SimpleCommandFactory
from libs import Steps, Nurse, Leader, Beds

steps = Steps()


class Command:
    def __init__(self, fn, txt):
        self.fn = fn
        self.txt = txt

    def execute(self, line, event):
        self.fn(line, event)


class Commands:
    def __init__(self, cmds):
        self.cmds = cmds

    def execute(self, line, event):
        txt = event.message.text
        for cmd in self.cmds:
            if cmd.txt == txt:
                cmd.execute(line, event)


def events_excute(event):
    line = LineAPI(event)
    global steps
    steps.run(line, event)
