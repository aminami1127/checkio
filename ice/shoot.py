import math


def calc_equation(crd1, crd2):
    a = (crd1[1] - crd2[1]) / (crd1[0] - crd2[0]) if crd1[0] != crd2[0] else 0
    b = crd1[1] - a * crd1[0]
    return lambda x: a * x + b, (a, b)


def calc_hitpoint(param1, param2):
    # y = a1 x + b1
    # y = a2 x + b2
    # 0 = (a1 - a2) x + (b1 - b2)
    # x = - (b1 - b2) / (a1 - a2)
    if param1[0] == param2[0]:
        return None  # ballistic is parallel to the wall
    x = - (param1[1] - param2[1]) / (param1[0] - param2[0])
    return x, param1[0] * x + param1[1]


def shot(wall1, wall2, shot_point, later_point):
    avg = lambda x, y: (x + y) / 2
    distance = lambda crd1, crd2: math.sqrt(sum((x[0] - x[1]) ** 2 for x in zip(crd1, crd2)))
    center = tuple(avg(c1, c2) for c1, c2 in zip(wall1, wall2))

    ballistic, param1 = calc_equation(shot_point, later_point)
    wall, param2 = calc_equation(wall1, wall2)
    hit_point = calc_hitpoint(param1, param2)
    wall_length = distance(wall1, wall2)
    score = calc_equation((0, 100), (wall_length / 2, 0))[0]

    def check_hit():
        # check direction
        direction = lambda crd1, crd2: tuple((x[0] - x[1]) for x in zip(crd1, crd2))
        d1, d2 = direction(later_point, shot_point), direction(hit_point, shot_point)
        if not all(y >= 0 for y in (x[0] / x[1] if x[1] else 0 for x in zip(d1, d2))):
            return False

        # check hit the wall
        if ballistic(wall1[0]) < wall1[1] or ballistic(wall2[0]) > wall2[1]:
            return False
        return True

    if hit_point and check_hit():
        return round(score(distance(center, hit_point)))
    else:
        return -1


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert shot((2, 2), (5, 7), (11, 2), (8, 3)) == 100, "1st case"
    #assert shot((2, 2), (5, 7), (11, 2), (7, 2)) == 0, "2nd case"
    #assert shot((2, 2), (5, 7), (11, 2), (8, 4)) == 29, "3th case"
    #assert shot((2, 2), (5, 7), (11, 2), (9, 5)) == -1, "4th case"
    #assert shot((2, 2), (5, 7), (11, 2), (10.5, 3)) == -1, "4th case again"
    #assert shot((10,10),(10,90),(50,90),(50,50))== -1, "4th case again"
    assert shot((10,10),(10,90),(70,60),(50,60))== 75, "4th case again"