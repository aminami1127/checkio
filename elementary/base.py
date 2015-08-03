from string import digits, ascii_uppercase


def checkio(str_number, radix):
    numbers = digits + ascii_uppercase
    if any(x for x in str_number if numbers.index(x)  >= radix):
        return -1
    else:
        return sum(radix ** i * numbers.index(x) for i, x in enumerate(str_number[::-1]))


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("909", 9) == -1 , "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A > 10"
