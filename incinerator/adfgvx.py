SYMBOLS = 'ADFGVX'


def divide(length, word):
    """divide the word by length size"""
    i = 0
    while True:
        sliced = word[i:i+length]
        if not sliced:
            break
        yield sliced.ljust(length)
        i += length


def uniqualize(keyword):
    """remove duplicate alphabet of keyword(order isn't changed)"""
    uniqued_key = ''
    for c in keyword:
        if c not in uniqued_key:
            uniqued_key += c
    return uniqued_key


def convert_square(secret_alphabet):
    return [x for x in divide(len(SYMBOLS), secret_alphabet)]


def encode(message, secret_alphabet, keyword):
    clean = lambda x: ''.join(y for y in x.lower() if y.isalnum())
    convert = convert_square(secret_alphabet)

    # convert message by secret_alphabet square
    converted = ''.join(
        ''.join(
            SYMBOLS[i] + SYMBOLS[row.index(c)]
            for i, row in enumerate(convert) if c in row
        )
        for c in clean(message)
    )

    # create matrix to encode message
    uniqued_key = uniqualize(keyword)
    matrix = [x for x in divide(len(uniqued_key), converted)]
    encoded = ''.join(
        ''.join(y for y in x[1] if y.isalpha()) for x in
        sorted(zip(uniqued_key, zip(*matrix)), key=lambda x: x[0])
    )
    return encoded


def decode(message, secret_alphabet, keyword):
    uniqued_key = uniqualize(keyword)
    # num of the characters that each key alphabet related
    size_of_keyalphas = zip(
        uniqued_key,
        [len([y for y in x if y.isalpha()])
         for x in zip(*divide(len(uniqued_key), message))]
    )

    # create matrix to decode original message
    i, sorted_matrix = 0, []
    for k, size in sorted(size_of_keyalphas, key=lambda x: x[0]):
        sorted_matrix.append(message[i:i+size])
        i += size
    matrix = list(
        x[1] for x in sorted(
            zip(sorted(uniqued_key), sorted_matrix), key=lambda x: keyword.index(x[0])
        )
    )
    # append white space to the matrix
    matrix = [x.ljust(max(len(x) for x in matrix)) for x in matrix]
    message = ''.join(
        ''.join(x) for x in zip(*matrix)
    ).strip()

    # decode each pair characters of the message by convert_square
    decoded = ''
    convert = convert_square(secret_alphabet)
    iter_message_pairs = zip(message, message[1:])
    for i, j in iter_message_pairs:
        decoded += convert[SYMBOLS.index(i)][SYMBOLS.index(j)]
        try:
            next(iter_message_pairs)
        except StopIteration:
            break
    return decoded


if __name__ == '__main__':
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'FXGAFVXXAXDDDXGA', "encode I am going"
    assert decode("FXGAFVXXAXDDDXGA",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'iamgoing', "decode I am going"
    assert encode("attack at 12:00 am",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy") == 'DGDDDAGDDGAFADDFDADVDVFAADVX', "encode attack"
    assert decode("DGDDDAGDDGAFADDFDADVDVFAADVX",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy") == 'attackat1200am', "decode attack"
    assert encode("ditiszeergeheim",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten") == 'DFGGXXAAXGAFXGAFXXXGFFXFADDXGA', "encode ditiszeergeheim"
    assert decode("DFGGXXAAXGAFXGAFXXXGFFXFADDXGA",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten") == 'ditiszeergeheim', "decode ditiszeergeheim"
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'DXGAXAAXXVDDFGFX', "encode weasel == weasl"
    assert decode("DXGAXAAXXVDDFGFX",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'iamgoing', "decode weasel == weasl"
