import itertools as it
import functools as ft


def euclidean(a, b):
    while b:
        c = b
        b = a % b
        a = c
    return a


def divisors(number):
    i = 1
    while i <= number:
        if not number % i:
            yield i
        i += 1


def greatest_common_divisor(*args):
    """
        Find the greatest common divisor
    """
    # find max number of each number pair gcd's divisors that can divide all input numbers.
    return max(
        ft.reduce(
            lambda x, y: x & y,
            [set(divisors(euclidean(*sorted(x, reverse=True)))) for x in it.combinations(args, 2)]
        )
    )


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert greatest_common_divisor(6, 4) == 2, "Simple"
    assert greatest_common_divisor(2, 4, 8) == 2, "Three arguments"
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1, "Prime numbers"
    assert greatest_common_divisor(3, 9, 3, 9) == 3, "Repeating arguments"
