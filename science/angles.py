import math
import itertools


def checkio(a, b, c):
    sides, angles = (a, b, c), []
    if not(abs(b - c) < a < b + c):
        return [0, 0, 0]
    for x, y in itertools.combinations(enumerate(sides), 2):
        z = [(i, w) for i, w in enumerate(sides) if i not in (x[0], y[0])][0]
        angles.append(math.degrees(math.acos((x[1] ** 2 + y[1] ** 2 - z[1] ** 2) / (2 * x[1] * y[1]))))
    return sorted(map(round, angles))


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    # assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    # assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    assert checkio(10, 20, 30) == [0, 0, 0], "It's can not be a triangle"

