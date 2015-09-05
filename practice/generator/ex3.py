# -*- coding:utf-8 -*-

sample = lambda x, y: (n ** 2 for n in range(x, y + 1))
print([x for x in sample(1, 10)])
