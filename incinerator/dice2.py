import itertools as it
import functools as ft
import random
from multiprocessing import Process, Manager

TRIAL = 1e+6


def worker(dice_number, sides, target, counts):
    roll = ft.partial(random.randrange, start=1, stop=sides + 1)
    count = 0
    for i in it.count(1):
        if i > TRIAL:
            counts.append(count)
            return counts
        if sum(roll() for _ in range(dice_number)) == target:
            count += 1


def probability(dice_number, sides, target):
    num_of_process = 20
    jobs = []
    manager = Manager()
    counts = manager.list()

    for i in range(num_of_process):
        p = Process(
            target=worker, args=(dice_number, sides, target, counts)
        )
        jobs.append(p)
        p.start()

    for proc in jobs:
        proc.join()
    return sum(counts) / (TRIAL * num_of_process)


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
