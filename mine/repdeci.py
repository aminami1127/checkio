def find_repeat(L):
    length = len(L)
    for i in range(length):
        for j in range(i, length):
            import itertools as it
            for k in it.count(1):
                if k > len(L):
                    break
                if L[i:j] * k == L[i:]:
                    return (i, j)
    return False


def convert(numerator, denominator):
    repeat_exists = False
    integer, decimal = str(numerator / denominator).split('.')
    # repeating part doesn't exist
    if len(decimal) < 16:
        if sum(map(int, decimal)):
            return '{}.{}'.format(integer, ''.join(decimal))
        else:
            # zero
            return integer + '.'
    else:
        decimal = decimal[:-1]
        repeat_exists = find_repeat(decimal * 2)
        # repeating part exists
        unique = decimal[:repeat_exists[0]]
        repeating = decimal[repeat_exists[0]:repeat_exists[1]]
        return '{}.{}'.format(
            integer, ''.join(unique) + '({})'.format(''.join(repeating))
        )


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert convert(1, 3) == "0.(3)", "1/3 Classic"
    #assert convert(5, 3) == "1.(6)", "5/3 The same, but bigger"
    #assert convert(3, 8) == "0.375", "3/8 without repeating part"
    assert convert(7, 11) == "0.(63)", "7/11 prime/prime"
    assert convert(29, 12) == "2.41(6)", "29/12 not and repeating part"
    assert convert(11, 7) == "1.(571428)", "11/7 six digits"
    assert convert(0, 117) == "0.", "Zero"
