from itertools import permutations as p


def checkio(words_set):
    pairs = [x for x in p(words_set, 2) if bool(set(x[0]) & set(x[1]))]
    return bool([x for x, y in pairs if x.endswith(y)])


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"
