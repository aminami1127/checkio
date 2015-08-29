from fractions import Fraction as F


def divide_pie(groups):
    den = sum(x if x > 0 else -x for x in groups)
    pie = F(den, den)
    for num in groups:
        pie = pie - F(num, den) if num > 0 else pie * (1 - F(-num, den))
    return (pie.numerator, pie.denominator) if pie.numerator else (0, 1)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance((2, -2), (tuple, list)), "Return tuple or list"
    assert tuple(divide_pie((2, -1, 3))) == (1, 18), "Example"
    assert tuple(divide_pie((1, 2, 3))) == (0, 1), "All know about the pie"
    assert tuple(divide_pie((-1, -1, -1))) == (8, 27), "One by one"
    assert tuple(divide_pie((10,))) == (0, 1), "All together"
