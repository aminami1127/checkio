# -*- coding:utf-8 -*-

def send_value_generator():
    i = (yield)
    while True:
        i = (yield i)


sample = send_value_generator()
next(sample)
print(sample.send('first'))
print(sample.send('second'))
print(sample.send('third'))
print(sample.send('fourth'))
print(sample.send('fifith'))
