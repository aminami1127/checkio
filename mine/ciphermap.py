import itertools as it


def recall_password(cipher_grille, ciphered_password):
    rotate = lambda L: tuple(map(lambda L: list(reversed(L)), zip(*L)))
    find_pass = lambda x, y: ''.join(z[1] for z in zip(x, y) if z[0] == 'X')
    password = ''
    for _ in range(len(cipher_grille)):
        password += find_pass(it.chain(*cipher_grille), it.chain(*ciphered_password))
        cipher_grille = rotate(cipher_grille)
    return password


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
