# -*- coding:utf-8 -*-

def sample_generator(start, end):
    for i in range(start, end + 1):
        yield i ** 2

sample = sample_generator(1, 10)
print([x for x in sample])
