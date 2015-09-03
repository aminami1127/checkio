# -*- coding:utf-8 -*-

def send_value_generator():
    i = (yield)
    while True:
        i = (yield i ** 2)


sample = send_value_generator()
next(sample)
print(sample.send(1))
print(sample.send(2))
print(sample.send(3))
print(sample.send(4))
print(sample.send(5))
