# -*- coding:utf-8 -*-

import itertools

infinite_generator = lambda x: (y ** 2 for y in itertools.count(x))

sample = infinite_generator(1)
for i in sample:
    print(i)
    if i > 1000:
        break
