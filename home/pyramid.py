def count_gold(pyramid):
    """
    Return max possible sum in a path from top to bottom
    """
    # max golds from top to each rooms
    max_golds = [[] for _ in range(len(pyramid))]
    for i, row in enumerate(pyramid):
        for j, gold in enumerate(row):
            if i > 0:
                left_upper_gold = max_golds[i - 1][j - 1] if j > 0 else 0
                right_upper_gold = max_golds[i - 1][j] if j < len(row) - 1 else 0
                max_golds[i].append(max(left_upper_gold, right_upper_gold) + gold)
            else:
                max_golds[i].append(gold)  # top room
    return max(max_golds[-1])





if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )) == 23, "First example"
    assert count_gold((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )) == 15, "Second example"
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18, "Third example"
