def iter_pigeons():
    i = 1
    while True:
        yield sum(range(1, i + 1))
        i += 1


def checkio(number):
    pigeons = iter_pigeons()
    feeded = 0
    while True:
        hungry = next(pigeons)
        if number <= hungry:
            return number if number > feeded else feeded
        else:
            number = number - hungry
            feeded = hungry



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert checkio(1) == 1, "1st example"
    #assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
