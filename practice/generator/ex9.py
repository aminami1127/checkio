# -*- coding:utf-8 -*-


def even_odd_generator():
    i = (yield)
    while True:
        i = (yield i)


sample = even_odd_generator()
next(sample)
print(sample.send('first'))
print(sample.send('second'))
print(sample.send('third'))
print(sample.send('fourth'))
print(sample.send('fifith'))
