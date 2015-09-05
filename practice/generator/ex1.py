# -*- coding:utf-8 -*-

class SampleIterator(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    # python3 => __next__(self):
    def next(self):
        if self.start > self.end:
            raise StopIteration
        ret = self.start ** 2
        self.start += 1
        return ret

sample = SampleIterator(1, 10)
print([x for x in sample])
print([x for x in sample])  # もうsampleは要素を返さない
sample = SampleIterator(2, 20)
print([x for x in sample])
