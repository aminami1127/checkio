import collections
import functools

Symbols = collections.namedtuple(
    'Symbols',
    ['unus', 'quinque', 'decem', 'quinquaginta', 'centum', 'quingenti', 'mille']
)
symbol = Symbols('I', 'V', 'X', 'L', 'C', 'D', 'M')


def to_roman(digit, one, five, ten):
    if 0 < digit < 4:
        return ''.join([one for _ in range(digit)])
    elif digit == 4:
        return one + five
    elif digit == 5:
        return five
    elif 5 < digit < 9:
        return five + ''.join([one for _ in range(digit - 5)])
    else:
        return one + ten

to_roman_one = functools.partial(
    to_roman, one=symbol.unus, five=symbol.quinque, ten=symbol.decem
)
to_roman_ten = functools.partial(
    to_roman, one=symbol.decem, five=symbol.quinquaginta, ten=symbol.centum
)
to_roman_hundred = functools.partial(
    to_roman, one=symbol.centum, five=symbol.quingenti, ten=symbol.mille
)


def checkio(number):
    roman = ''
    thousand, remain = number // 1000, number % 1000
    if thousand:
        roman += ''.join([symbol.mille for _ in range(thousand)])
    hundred, remain = remain // 100, remain % 100
    if hundred:
        roman += to_roman_hundred(hundred)
    ten, one = remain // 10, remain % 10
    if ten:
        roman += to_roman_ten(ten)
    if one:
        roman += to_roman_one(one)
    return roman



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
