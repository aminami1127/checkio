def checkio(anything):
    class Always(object):
        def __eq__(self, arg):
            return True

        def __ne__(self, arg):
            return True

        def __lt__(self, arg):
            return True

        def __le__(self, arg):
            return True

        def __gt__(self, arg):
            return True

        def __ge__(self, arg):
            return True

    return Always()


if __name__ == '__main__':
    import re
    import math

    assert checkio({}) != [],         'You'
    assert checkio('Hello') < 'World', 'will'
    assert checkio(80) > 81,           'never'
    assert checkio(re) >= re,          'make'
    assert checkio(re) <= math,        'this'
    assert checkio(5) == ord,          ':)'

    print('NO WAY :(')
