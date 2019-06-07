class Steps:
    DEBUG = False

    def debug_or_input(self, defaultstr, debugoutput):
        return debugoutput if self.DEBUG else input(defaultstr)

    def step1(self):
        self.beds = Beds()
        self.beds.display_index()
        indeces = self.debug_or_input('請輸入沒有病床的編號(空格分割) ps:左邊 : ', '30 20 15')
        indeces = list(map(int, indeces.split()))
        deleted_list = []
        for index in indeces:
            deleted_list.append(self.beds.del_by_index(index))
        print('被刪除號碼為 : {}  剩下床數: {}'.format(" ".join(deleted_list), len(self.beds.data)))

    def step2(self):
        while True:
            nurse_count = self.debug_or_input('請輸入神聖護理師的數目: ', '5')
            nurse_count = int(nurse_count)
            nums = self.debug_or_input('請輸入分配數量(空格分割): ', '9 9 9 9 9')
            nums = list(map(int, nums.split()))
            if len(nums) != nurse_count or sum(nums) != len(self.beds.data):
                print('輸入數量錯誤 請重新輸入: sum:{} beds: {}'.format(sum(nums), len(self.beds.data)))
                continue
            break

        self.nurses = [Nurse(num) for num in nums]

    def step3(self):
        leader = Leader()
        leader.compare(self.nurses, self.beds)

    def run(self):
        fnsstr = [fnstr for fnstr in dir(self) if fnstr.startswith('step') and callable(getattr(self, fnstr))]
        fnsstr = sorted(fnsstr)
        for fnstr in fnsstr:
            fn = getattr(self, fnstr)
            fn()


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
        for i, d in enumerate(self.data):
            print("{})-{}".format(i, d))


class Nurse:
    def __init__(self, count):
        self.count = count
        self.beds = []

    def is_full(self):
        return self.count <= len(self.beds)

    def add_bed(self, bed):
        self.beds.append(bed)

    def display(self):
        print('人數: {} 床: {}'.format(self.count, " ".join(self.beds)))


class Leader:
    def compare(self, nurses, beds):
        n_i = 0
        for bed in beds.data:
            nurse = nurses[n_i]
            nurse.add_bed(bed)
            if nurse.is_full():
                n_i += 1
        for n in nurses:
            n.display()


if __name__ == '__main__':
    # b = Beds()
    # b.display_index()
    s = Steps()
    s.DEBUG = False
    s.run()
