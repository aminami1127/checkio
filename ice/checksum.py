import functools


def map_point(val):
    double = val * 2
    if double < 10:
        return double
    else:
        return functools.reduce(lambda x, y: x + y, map(int, str(double)))


def checkio(data):
    charseq = lambda x: ord(x) - 48
    clean = lambda L: [x for x in L if x.isalpha() or x.isdigit()]
    total = sum(
        x if i % 2 else map_point(x)
        for i, x in enumerate(map(charseq, reversed(clean(data))))
    )
    mod = total % 10
    final = 10 - mod if mod else 0
    return [str(final), total]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio("799 273 9871") == ["3", 67]), "First Test"
    assert (checkio("139-MT") == ["8", 52]), "Second Test"
    assert (checkio("123") == ["0", 10]), "Test for zero"
    assert (checkio("999_999") == ["6", 54]), "Third Test"
    assert (checkio("+61 820 9231 55") == ["3", 37]), "Fourth Test"
    assert (checkio("VQ/WEWF/NY/8U") == ["9", 201]), "Fifth Test"
