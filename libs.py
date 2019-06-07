class Steps:
    def __init__(self):
        self.fn = self.step1

    def step1(self, line, event, txt):
        if txt.lower() != 'go':
            line.reply('???')
            return
        self.beds = Beds()
        msg = self.beds.display_index()
        msg += '請輸入沒有病床的編號(空格分割) ps:左邊 : '
        line.reply(msg)
        self.fn = self.step2

    def step2(self, line, event, txt):
        indeces = txt
        indeces = list(map(int, indeces.split()))
        deleted_list = []
        for index in indeces:
            deleted_list.append(self.beds.del_by_index(index))
        msg = '被刪除號碼為 : {}  剩下床數: {}'.format(" ".join(deleted_list), len(self.beds.data))
        self.step2_1(line, event, txt, prefix_msg=msg)

    def step2_1(self, line, event, txt, prefix_msg=''):
        msg = prefix_msg + '\n請輸入神聖護理師的數目: '
        msg = msg.strip('\n')
        line.reply(msg)
        self.fn = self.step3

    def step3(self, line, event, txt):
        nurse_count = txt
        nurse_count = int(nurse_count)
        line.reply('請輸入分配數量(空格分割): ')
        self.nurses_count = nurse_count
        self.fn = self.step4

    def step4(self, line, event, txt):
        nums = txt
        nums = list(map(int, nums.split()))
        if len(nums) != self.nurses_count or sum(nums) != len(self.beds.data):
            print()
            msg = '輸入數量錯誤 請重新輸入: sum:{} beds: {}'.format(sum(nums), len(self.beds.data))
            line.reply(msg)
            self.fn = self.step2_1
            return

        self.nurses = [Nurse(num) for num in nums]
        leader = Leader()
        msg = leader.compare(self.nurses, self.beds)
        line.reply(msg)
        self.fn = self.step1

    def run(self, line, event):
        txt = event.message.text
        if txt.lower() == 'go':
            self.fn = self.step1
        fn = self.fn
        fn(line, event, txt)


class Beds:
    def __init__(self):
        data = []
        data.extend(self.generate([28], 1))
        data.extend(self.generate(range(29, 31 + 1), 3))
        data.extend(self.generate(range(32, 34 + 1), 2))
        data.extend(self.generate(range(35, 40 + 1), 1))
        data.extend(self.generate(range(41, 48 + 1), 3))
        data.extend(self.generate(range(26, 27 + 1), 1))
        self.data = data

    def generate(self, numbers, area_count):
        import string
        ret = []
        letters = string.ascii_uppercase
        for num in numbers:
            if area_count == 1:
                ret.append(str(num))
            else:
                for i in range(area_count):
                    c = letters[i]
                    ret.append(str(num) + c)
        return ret

    def del_by_index(self, index):
        ret = self.data[index]
        del self.data[index]
        return ret

    def display_index(self):
        msg = ''
        for i, d in enumerate(self.data):
            print()
            msg += "{})-{}\n".format(i, d)
        return msg


class Nurse:
    def __init__(self, count):
        self.count = count
        self.beds = []

    def is_full(self):
        return self.count <= len(self.beds)

    def add_bed(self, bed):
        self.beds.append(bed)

    def display(self):
        print()
        return '人數: {} 床: {}'.format(self.count, " ".join(self.beds))


class Leader:
    def compare(self, nurses, beds):
        n_i = 0
        msg_list = []
        for bed in beds.data:
            nurse = nurses[n_i]
            nurse.add_bed(bed)
            if nurse.is_full():
                n_i += 1
        for n in nurses:
            msg_list.append(n.display())
        return "\n".join(msg_list)


if __name__ == '__main__':
    # b = Beds()
    # b.display_index()
    s = Steps()
    s.DEBUG = False
    s.run()
