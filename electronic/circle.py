import math


def center_R(x1, y1, x2, y2, x3, y3):
    s = 2 * ((y1 - y3) * (x1 - x2) - (y1 - y2) * (x1 - x3))
    x = ((y1 - y3) * (y1 ** 2 - y2 ** 2 + x1 ** 2 - x2 ** 2) - (y1 - y2) * (y1 ** 2 - y3 ** 2 + x1 ** 2 - x3 ** 2)) / s
    y = ((x1 - x3) * (x1 ** 2 - x2 ** 2 + y1 ** 2 - y2 ** 2) - (x1 - x2) * (x1 ** 2 - x3 ** 2 + y1 ** 2 - y3 ** 2)) / -s
    R = math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
    return (x, y), R


def checkio(data):
    (x1, y1), (x2, y2), (x3, y3) = eval(data)
    (x0, y0), R = center_R(x1, y1, x2, y2, x3, y3)
    trim = lambda x: '-' + str(round(x, 2)).rstrip('0').rstrip('.') if x >= 0 \
        else '+' + str(round(x, 2)).rstrip('0').rstrip('.')
    return '(x{})^2+(y{})^2={}^2'.format(trim(x0), trim(y0), trim(R).replace('-', ''))


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    # assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
    assert checkio("(2,2),(1,4),(2,5)") == "(x-2.5)^2+(y-3.5)^2=1.58^2"
