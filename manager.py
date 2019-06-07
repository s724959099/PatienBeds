from line_api import LineAPI
from util.commands import Invoker, SimpleCommandFactory
from libs import Steps, Nurse, Leader, Beds

steps = Steps()


def go(line, event):
    global s
    s = Steps()
    message = 'demo1'
    line.reply(message)


def go1(line, event):
    global s
    message = s.a
    line.reply(message)


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
    # commands = [
    #     SimpleCommandFactory(demo, 'demo')
    # ]
    # cmds = Commands([
    #     Command(go, 'go'),
    #     Command(go1, 'go1'),
    # ])
    # cmds.execute(line, event)

    # invoker = Invoker()
    # invoker.appends(commands)
    # invoker.execute(execute_all=True, event=event, line=line)
