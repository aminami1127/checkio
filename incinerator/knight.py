import itertools as it
from string import ascii_lowercase as alpha


def checkio(cells):
    """str -> int
    Number of moves in the shortest path of knight
    """
    restrict = lambda c: 0 < c[0] < 9 and 0 < c[1] < 9
    calc_reachable = lambda a, b: list(
        filter(restrict, it.chain(
            ((a + x, b + y) for x in (-2, 2) for y in (-1, 1)),
            ((a + x, b + y) for y in (-2, 2) for x in (-1, 1)),
        )))
    to_num = lambda x: alpha.index(x) + 1 if x.isalpha() else int(x)
    start, goal = (tuple(map(to_num, x)) for x in cells.split('-'))
    reachable = (start,)
    for count in it.count(1):
        reachable = set(it.chain.from_iterable(
            calc_reachable(*c) for c in reachable
        ))
        if goal in reachable:
            return count


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("b1-d5") == 2, "1st example"
    assert checkio("a6-b8") == 1, "2nd example"
    assert checkio("h1-g2") == 4, "3rd example"
    assert checkio("h8-d7") == 3, "4th example"
    assert checkio("a1-h8") == 6, "5th example"
