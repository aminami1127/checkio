import itertools as it


def decode_amsco(message, key):
    key = str(key)
    key_len, mes_len = len(key), len(message)

    def slice_message(cut):
        i = 0
        nonlocal message
        for c in cut:
            yield message[i:i + c]
            i += c
        message = message[sum(cut):]

    # calc how many chars in each matrix cell
    key_matrix, remain = [], mes_len
    for i in it.count(0):
        onetwo = it.cycle((1, 2))
        if remain < 0:
            break
        char_lens = list(it.islice(onetwo, i, i + key_len))
        total = sum(char_lens)
        if remain < total:
            char_lens = []
            for j in range(i, i + key_len):
                onetwo = it.cycle((1, 2))
                if not remain:
                    size = 0
                elif remain == 1:
                    size = 1
                else:
                    size = list(it.islice(onetwo, j, j + 1))[0]
                char_lens.append(size)
                remain -= size
        key_matrix.append(char_lens)
        remain -= total

    # pairs of key character and character size matrix column
    key_matrix = sorted(
        list(zip(key, zip(*key_matrix))),
        key=lambda x: x[0]
    )
    # slice message by each matrix column number and sort column by key order
    key_matrix = [
        x[1] for x in
        sorted(
            [(x[0], list(slice_message(x[1]))) for i, x in enumerate(key_matrix)],
            key=lambda x: key.index(x[0])
        )
    ]
    return ''.join(
        ''.join(x) for x in zip(*key_matrix)
    )


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert decode_amsco("oruoreemdstmioitlpslam", 4123) == "loremipsumdolorsitamet", "Lorem Ipsum"
    assert decode_amsco('kicheco', 23415) == "checkio", "Checkio"
    assert decode_amsco('hrewhoorrowyilmmmoaouletow', 123) == "howareyouwillhometommorrow", "How are you"
