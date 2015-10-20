def convert(numerator, denominator):
    to_str = lambda L: ''.join(map(str, L))
    decimals, remains = [], []
    integer, remain = numerator // denominator, numerator % denominator
    remains.append(remain)
    while True:
        quotient, remain = remain * 10 // denominator, remain * 10 % denominator
        decimals.append(quotient)
        if not remain:
            # doesn't repeat
            if sum(decimals):
                return '{}.{}'.format(integer, to_str(decimals))
            else:
                return '{}.'.format(integer)
        if remain in remains:
            # repeat found
            repeat_start = remains.index(remain)
            non_repeat, repeat = decimals[:repeat_start], decimals[repeat_start:]
            return '{}.{}'.format(
                integer, to_str(non_repeat) + '({})'.format(to_str(repeat))
            )
        else:
            remains.append(remain)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert convert(1, 3) == "0.(3)", "1/3 Classic"
    assert convert(5, 3) == "1.(6)", "5/3 The same, but bigger"
    assert convert(3, 8) == "0.375", "3/8 without repeating part"
    assert convert(7, 11) == "0.(63)", "7/11 prime/prime"
    assert convert(29, 12) == "2.41(6)", "29/12 not and repeating part"
    assert convert(11, 7) == "1.(571428)", "11/7 six digits"
    assert convert(0, 117) == "0.", "Zero"
