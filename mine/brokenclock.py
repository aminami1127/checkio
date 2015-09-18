from datetime import datetime, timedelta
import re


def to_sec(unit):
    dct = {'second': 1, 'minute': 60, 'hour': 3600}
    m = re.compile('^(second|minute|hour)')
    return dct[m.match(unit).group()]


def broken_clock(starting_time, wrong_time, error_description):
    a, b, c, d = error_description.replace('at ', '').split()
    err_per_sec = (int(a) * to_sec(b)) / (int(c) * to_sec(d))
    time_diff_sec = lambda x, y: sum((int(k) - int(j)) * (60 ** i)
                                     for i, (j, k) in enumerate(
                                     reversed(
                                         list(zip(x.split(':'), y.split(':')))
                                     )))
    elapsed_sec = int(time_diff_sec(starting_time, wrong_time)) / (1 + err_per_sec)
    return datetime.strftime(
        datetime.strptime(starting_time, '%H:%M:%S') + timedelta(seconds=elapsed_sec),
        '%H:%M:%S'
    )


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert broken_clock('00:00:00', '00:00:15', '+5 seconds at 10 seconds') == '00:00:10', "First example"
    assert broken_clock('06:10:00', '06:10:15', '-5 seconds at 10 seconds') == '06:10:30', 'Second example'
    assert broken_clock('13:00:00', '14:01:00', '+1 second at 1 minute') == '14:00:00', 'Third example'
    assert broken_clock('01:05:05', '04:05:05', '-1 hour at 2 hours') == '07:05:05', 'Fourth example'
    assert broken_clock('00:00:00', '00:00:30', '+2 seconds at 6 seconds') == '00:00:22', 'Fifth example'
