# -*- coding:utf-8 -*-

import itertools

even_odd_generator = lambda: ('odd' if i % 2 else 'even' for i, x in enumerate(itertools.count(1)))

sample = even_odd_generator()
for i, x in enumerate(sample):
    print(x)
    if i > 1000:
        break
