def convert(numerator, denominator):
    sequence = []
    integer, decimal = str(numerator / denominator).split('.')
    digit = decimal[0]
    while digit not in sequence:
        sequence.append(digit)
        decimal = decimal[1:]
        # repeating part doesn't exist
        if not decimal:
            if sum(map(int, sequence)):
                return '{}.{}'.format(integer, ''.join(sequence))
            else:
                return integer + '.'
        else:
            digit = decimal[0]
    else:
        # repeating part exists
        repeat_start = sequence.index(digit)
        unique, repeating = sequence[:repeat_start], sequence[repeat_start:]
        return '{}.{}'.format(
            integer, ''.join(unique) + '({})'.format(''.join(repeating))
        )


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert convert(1, 3) == "0.(3)", "1/3 Classic"
    assert convert(5, 3) == "1.(6)", "5/3 The same, but bigger"
    assert convert(3, 8) == "0.375", "3/8 without repeating part"
    assert convert(7, 11) == "0.(63)", "7/11 prime/prime"
    assert convert(29, 12) == "2.41(6)", "29/12 not and repeating part"
    assert convert(11, 7) == "1.(571428)", "11/7 six digits"
    assert convert(0, 117) == "0.", "Zero"
