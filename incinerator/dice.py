import itertools as it


def probability(dice_number, sides, target):
    deno = sides ** dice_number
    nume = len(list(
        filter(lambda x: sum(x) == target,
               it.product(range(1, min(sides + 1, target)), repeat=dice_number))
    ))
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
