import itertools as it
from math import ceil, hypot


def checkio(radius):
    """count tiles"""
    crds = [
        ((x1, y1), (x2, y2)) for x1, y1, x2, y2 in it.product(range(ceil(radius + 1)), repeat=4)
        if x2 == x1 + 1 and y2 == y1 + 1
    ]
    # p: lower left coordinate of each squares
    # q: upper right coordinate of each squares
    solid = sum(1 for p, q in crds if hypot(*q) <= radius) * 4
    partial = sum(1 for p, q in crds if hypot(*p) < radius < hypot(*q)) * 4
    return [solid, partial]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(2) == [4, 12], "N=2"
    assert checkio(3) == [16, 20], "N=3"
    assert checkio(2.1) == [4, 20], "N=2.1"
    assert checkio(2.5) == [12, 20], "N=2.5"
