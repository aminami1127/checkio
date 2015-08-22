from string import ascii_uppercase as alpha
import itertools as it


def decrypt(enc_alpha, key_alpha):
    if alpha.index(enc_alpha) >= alpha.index(key_alpha):
        return alpha[alpha.index(enc_alpha) - alpha.index(key_alpha)]
    else:
        return alpha[len(alpha) + alpha.index(enc_alpha) - alpha.index(key_alpha)]


def find_key(repeated):
    length = 1
    while length <= len(repeated):
        check, iter_key = '', it.cycle(repeated[:length])
        for _ in range(len(repeated)):
            check += next(iter_key)
        if repeated == check:
            return repeated[:length]
        else:
            length += 1


def decode_vigenere(old_decrypted, old_encrypted, new_encrypted):
    decrypted = lambda encrypted, key: ''.join(decrypt(*x) for x in zip(encrypted, it.cycle(key)))
    key = find_key(decrypted(old_encrypted, old_decrypted))
    return decrypted(new_encrypted, key)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert decode_vigenere('DONTWORRYBEHAPPY',
                           'FVRVGWFTFFGRIDRF',
                           'DLLCZXMFVRVGWFTF') == "BEHAPPYDONTWORRY", "CHECKIO"
    assert decode_vigenere('HELLO', 'OIWWC', 'ICP') == "BYE", "HELLO"
    assert decode_vigenere('LOREMIPSUM',
                          'OCCSDQJEXA',
                          'OCCSDQJEXA') == "LOREMIPSUM", "DOLORIUM"
