# -*- coding:utf-8 -*-


class SampleEvenOdd(object):
    def __init__(self):
        self.i = 0

    def __iter__(self):
        return self

    # python3 => __next__(self):
    def next(self):
        self.i += 1
        while True:
            if self.i % 2:
                return 'odd'
            else:
                return 'even'

sample = SampleEvenOdd()
for i, x in enumerate(sample):
    print(x)
    if i > 1000:
        break
