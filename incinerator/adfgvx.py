def encode(message, secret_alphabet, keyword):
    clean = lambda x: ''.join(y for y in x.lower() if y.isalnum())
    SYMBOLS = 'ADFGVX'

    def divide(length, word):
        i = 0
        for _ in range(length):
            sliced = word[i:i+length]
            if not sliced:
                break
            yield sliced.ljust(length)
            i += length

    matrix = [x for x in divide(len(SYMBOLS), secret_alphabet)]
    converted = ''.join(
        ''.join(SYMBOLS[i] + SYMBOLS[row.index(c)] for i, row in enumerate(matrix) if c in row)
        for c in clean(message)
    )
    unique_key = ''
    for c in keyword:
        if c not in unique_key:
            unique_key += c
    new_matrix = [x for x in divide(len(unique_key), converted)]
    encoded = ''.join(
        ''.join(y for y in x[0] if y.isalpha()) for x in
        sorted(zip(zip(*new_matrix), unique_key), key=lambda x: x[1])
    )
    return encoded


def decode(message, secret_alphabet, keyword):
    return message


if __name__ == '__main__':
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'FXGAFVXXAXDDDXGA', "encode I am going"
    # assert decode("FXGAFVXXAXDDDXGA",
    #               "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
    #               "cipher") == 'iamgoing', "decode I am going"
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
