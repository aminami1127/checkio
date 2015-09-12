def cofactor(matrix, row_num, col_num):
    cols = [col for i, col in enumerate(matrix) if i != col_num]
    rows = [row for i, row in enumerate(zip(*cols)) if i != row_num]
    return list(zip(*rows))


def checkio(matrix):
    if len(matrix) == 1:
        return matrix[0][0]

    elif len(matrix) == 2:
        a, b, c, d = matrix[0][0], matrix[1][0], matrix[0][1], matrix[1][1]
        return a * d - b * c

    else:
        sign = lambda i: -1 if i % 2 else 1
        return sum(
            matrix[j][0] * checkio(cofactor(matrix, 0, j)) * sign(i) for i, j in enumerate(range(len(matrix)))
        )


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[4, 3], [6, 3]]) == -6, 'First example'

    assert checkio([[1, 3, 2],
                    [1, 1, 4],
                    [2, 2, 1]]) == 14, 'Second example'
