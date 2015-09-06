import math


def calc_hitpoint(crd1, direction1, crd2, direction2):
    (a, b), (c, d) = crd1, crd2
    (d1, d2), (d3, d4) = direction1, direction2
    if d1 * d4 == d2 * d3:
        return None, None  # parralel lines
    k = ((b - d) * d3 - (a - c) * d4) / (d1 * d4 - d2 * d3)
    return (a + d1 * k, b + d2 * k), k


def calc_equation(crd1, crd2):
    a = (crd1[1] - crd2[1]) / (crd1[0] - crd2[0])
    b = crd1[1] - a * crd1[0]
    return lambda x: a * x + b


def shot(wall1, wall2, shot_point, later_point):
    avg = lambda x, y: (x + y) / 2
    direction = lambda crd1, crd2: tuple((x[0] - x[1]) for x in zip(crd1, crd2))
    distance = lambda crd1, crd2: math.sqrt(sum((x[0] - x[1]) ** 2 for x in zip(crd1, crd2)))

    ballistic, wall = direction(later_point, shot_point), direction(wall2, wall1)
    hit_point, k = calc_hitpoint(shot_point, ballistic, wall1, wall)

    if k and k > 0 and all(
        sorted(w)[0] <= hit_point[i] <= sorted(w)[1] for i, w in enumerate(zip(wall1, wall2))
    ):
        center = tuple(avg(c1, c2) for c1, c2 in zip(wall1, wall2))
        score = calc_equation((0, 100), (distance(wall1, wall2) / 2, 0))
        return round(score(distance(center, hit_point)))
    else:
        return -1


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert shot((2, 2), (5, 7), (11, 2), (8, 3)) == 100, "1st case"
    assert shot((2, 2), (5, 7), (11, 2), (7, 2)) == 0, "2nd case"
    assert shot((2, 2), (5, 7), (11, 2), (8, 4)) == 29, "3th case"
    assert shot((2, 2), (5, 7), (11, 2), (9, 5)) == -1, "4th case"
    assert shot((2, 2), (5, 7), (11, 2), (10.5, 3)) == -1, "4th case again"
