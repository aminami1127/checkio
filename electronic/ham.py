from itertools import zip_longest

def checkio(n, m):
    return sum(int(x) ^ int(y) for x, y in zip_longest(reversed(bin(n)[2:]), reversed(bin(m)[2:]), fillvalue=0))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
