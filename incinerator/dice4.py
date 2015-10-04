def probability(dice_number, sides, target):
    deno = sides ** dice_number
    nume = 0

    def loop(i, nest=dice_number - 1):
        nonlocal nume
        for j in range(1, sides + 1):
            if i + j >= target and nest != 1:
                break
            elif i + j == target and nest == 1:
                if not nume % 1000000:
                    print(nume)
                nume += 1
            if not nest - 1:
                continue
            else:
                loop(i + j, nest=nest - 1)

    for i in range(1, sides + 1):
        loop(i)
    return nume / deno


if __name__ == '__main__':
    #These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert(almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert(almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert(almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert(almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert(almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert(almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert(almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
