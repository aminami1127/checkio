from itertools import chain


def checkio(rows):
    cols = [x for x in zip(*rows)]
    diags = []
    loop = (len(rows) - 1) * 2 + 1
    for i in range(loop):
        if i < len(rows):
            diags.append([rows[j][i - j] for j in range(i + 1)])
            diags.append([rows[j][j - i - 1] for j in range(i + 1)])
        else:
            diags.append([rows[i - loop + j - 1][j - 1] for j in range(1, loop - i + 1)])
            diags.append([rows[i - loop + j - 1][-j] for j in range(1, loop - i + 1)])
    return any(x for x in chain(rows, cols, diags) if any(len(set(x[i:i+4])) == 1 for i in range(len(x) - 3)))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
