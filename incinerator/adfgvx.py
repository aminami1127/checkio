SYMBOLS = 'ADFGVX'


def divide(length, word):
    i = 0
    for _ in range(length):
        sliced = word[i:i+length]
        if not sliced:
            break
        yield sliced.ljust(length)
        i += length


def uniqualize(keyword):
    uniqued_key = ''
    for c in keyword:
        if c not in uniqued_key:
            uniqued_key += c
    return uniqued_key


def encode(message, secret_alphabet, keyword):
    clean = lambda x: ''.join(y for y in x.lower() if y.isalnum())

    matrix = [x for x in divide(len(SYMBOLS), secret_alphabet)]
    converted = ''.join(
        ''.join(SYMBOLS[i] + SYMBOLS[row.index(c)] for i, row in enumerate(matrix) if c in row)
        for c in clean(message)
    )
    uniqued_key = uniqualize(keyword)
    new_matrix = [x for x in divide(len(uniqued_key), converted)]
    encoded = ''.join(
        ''.join(y for y in x[1] if y.isalpha()) for x in
        sorted(zip(uniqued_key, zip(*new_matrix)), key=lambda x: x[0])
    )
    return encoded


def decode(message, secret_alphabet, keyword):
    uniqued_key = uniqualize(keyword)
    length = len(uniqued_key)
    key_contains_size = zip(
        uniqued_key,
        [len([y for y in x if y.isalpha()]) for x in zip(*divide(length, message))]
    )
    i, matrix = 0, []
    for k, size in sorted(key_contains_size, key=lambda x: x[0]):
        matrix.append(message[i:i+size])
        i += size
    tmp = list(
        x[1].ljust(3) for x in
        sorted(zip(sorted(uniqued_key), matrix), key=lambda x: keyword.index(x[0]))
    )
    tmp = ''.join(''.join(x) for x in zip(*tmp)).strip()
    decoded = ''
    matrix = [x for x in divide(len(SYMBOLS), secret_alphabet)]
    iter_tmp = zip(tmp, tmp[1:])
    for i, j in iter_tmp:
        decoded += matrix[SYMBOLS.index(i)][SYMBOLS.index(j)]
        try:
            next(iter_tmp)
        except:
            break
    return decoded


if __name__ == '__main__':
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'FXGAFVXXAXDDDXGA', "encode I am going"
    assert decode("FXGAFVXXAXDDDXGA",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'iamgoing', "decode I am going"
    # assert encode("attack at 12:00 am",
    #               "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
    #               "privacy") == 'DGDDDAGDDGAFADDFDADVDVFAADVX', "encode attack"
    # assert decode("DGDDDAGDDGAFADDFDADVDVFAADVX",
    #               "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
    #               "privacy") == 'attackat1200am', "decode attack"
    # assert encode("ditiszeergeheim",
    #               "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
    #               "piloten") == 'DFGGXXAAXGAFXGAFXXXGFFXFADDXGA', "encode ditiszeergeheim"
    # assert decode("DFGGXXAAXGAFXGAFXXXGFFXFADDXGA",
    #               "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
    #               "piloten") == 'ditiszeergeheim', "decode ditiszeergeheim"
    # assert encode("I am going",
    #               "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
    #               "weasel") == 'DXGAXAAXXVDDFGFX', "encode weasel == weasl"
    # assert decode("DXGAXAAXXVDDFGFX",
    #               "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
    #               "weasel") == 'iamgoing', "decode weasel == weasl"
