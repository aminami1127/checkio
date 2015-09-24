import math


def super_root(number):
    # Newton's method
    # f  = xlogx - logN
    # f' = logx + 1
    # x(n+1) = x(n) - f/f'
    f = lambda x: x * math.log(x) - math.log(number)
    _f = lambda x: math.log(x) + 1
    a = 1
    while True:
        b = a - (f(a) / _f(a))
        if abs(b - a) < 1e-6:
            return b
        else:
            a = b


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def check_result(function, number):
        result = function(number)
        if not isinstance(result, (int, float)):
            print("The result should be a float or an integer.")
            return False
        p = result ** result
        if number - 0.001 < p < number + 0.001:
            return True
        return False
    assert check_result(super_root, 4), "Square"
    assert check_result(super_root, 9), "Cube"
    assert check_result(super_root, 81), "Eighty one"
