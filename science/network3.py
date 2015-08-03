from itertools import count
from collections import Counter


def capture(matrix):
    security = Counter({i: row[i] for i, row in enumerate(matrix)})
    connected = lambda i: {j for j, x in enumerate(matrix[i]) if x and i != j}
    reached = {0}
    for time in count(1):
        reached.update(*map(connected, [k for k, v in security.items() if v == 0]))
        for i in reached: security.subtract({i: 1})  # attack
        if not list(security.elements()): return time


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"
