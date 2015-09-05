# -*- coding:utf-8 -*-

def infinite_generator(start):
    while True:
        yield start ** 2
        start += 1

sample = infinite_generator(1)
for i in sample:
    print(i)
    if i > 1000:
        break
