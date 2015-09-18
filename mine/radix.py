from string import ascii_uppercase as alpha
import itertools

MAX_K = 37


def checkio(number):
    to_int = lambda x: int(x) if x.isdigit() else alpha.index(x) + 10
    digits = list(map(to_int, number))
    k = max(digits) + 1
    for k in itertools.count(k):
        if k > MAX_K:
            return 0
        else:
            decimal = sum((k ** i) * x for i, x in enumerate(reversed(digits)))
            if not decimal % (k - 1):
                return k


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("18") == 10, "Simple decimal"
    assert checkio("1010101011") == 2, "Any number is divisible by 1"
    assert checkio("222") == 3, "3rd test"
    assert checkio("A23B") == 14, "It's not a hex"
    assert checkio("IDDQD") == 0, "k is not exist"
    print('Local tests done')
