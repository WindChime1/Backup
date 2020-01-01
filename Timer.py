import time as t
class MyTimer:
    def __init__(self):
        self.unit = ['年','月','日','时','分','秒']
        self.prompt = '未开始计时'
        self.last = []
        self.begin = 0
        self.end = 0
    def start(self):
        self.begin = t.localtime()
        print('开始计时')
    def stop(self):
        self.end = t.localtime()
        print('计时结束')
        self.calc()
    def calc(self):
        self.last = []
        self.prompt = '共运行了'
        for each in range(6):
            self.last.append(self.end[each]-self.begin[each])
        self.prompt+= (str(self.last[each]) +self.unit[each])
        print(self.prompt)
    def __str__(self):
        return self.prompt
    __repr__ = __str__
