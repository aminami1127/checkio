import itertools
import math


def total_cost(calls):
    cost = lambda t: t if t <= 100 else 100 + (t - 100) * 2
    minitue = lambda s: math.ceil(s / 60)
    day_total = lambda L: sum(minitue(int(x.split(' ')[-1])) for x in L)
    calls_per_day = itertools.groupby(calls, key=lambda x: x.split()[0])
    return sum(cost(day_total(x[1])) for x in calls_per_day)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost(("2014-02-05 01:00:00 1",
                       "2014-02-05 02:00:00 1",
                       "2014-02-05 03:00:00 1",
                       "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost(("2014-02-05 01:00:00 60",
                       "2014-02-05 02:00:00 60",
                       "2014-02-05 03:00:00 60",
                       "2014-02-05 04:00:00 6000")) == 106, "Precise calls"
