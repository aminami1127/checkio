GRID_SIZE = 4


def join_lines(lines_list):
    for line1 in lines_list:
        for line2 in lines_list:
            if line1[1] == line2[0]:
                lines_list.append([line1[0], line2[1]])
    return lines_list


def iter_squares():
    four_lines = lambda l: ([x, x + l], [x, x + GRID_SIZE * l],
                            [x + GRID_SIZE * l, x + (GRID_SIZE + 1) * l],
                            [x + l, x + (GRID_SIZE + 1) * l])
    dots = [1, 2, 3, 5, 6, 7, 9, 10, 11]
    for l in range(3):
        d = dots[:-l*3] if l else dots
        for x in d:
            yield four_lines(l + 1)


def find_squares(lines_list):
    for x in iter_squares():
        if all(y in lines_list for y in x):
            yield True


def checkio(lines_list):
    """Return the quantity of squares"""
    _sorted = list(map(sorted, lines_list))
    horizons = [x for x in _sorted if abs(x[0] - x[1]) == 1]
    virticals = [x for x in _sorted if abs(x[0] - x[1]) == GRID_SIZE]
    return len(list(find_squares(join_lines(horizons) + join_lines(virticals))))


if __name__ == '__main__':
    assert (checkio([[16,15],[16,12],[15,11],[11,12],[11,10],[10,14],[9,10],[14,13],[13,9],[15,14]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                    [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"
