# -*- coding:utf-8 -*-


def even_odd_generator():
    i = 1
    while True:
        if i % 2:
            yield 'odd'
        else:
            yield 'even'
        i += 1  # generatorではyieldした後もの処理も次の呼び出しで実行される

sample = even_odd_generator()
for i, x in enumerate(sample):
    print(x)
    if i > 1000:
        break
