import itertools


def calc_coefficient(x, y):
    score = 0
    if x[0] == y[0]: score += 10
    if x[-1] == y[-1]: score += 10
    score += (len(x) / len(y)) * 30 if len(x) <= len(y) else (len(y) / len(x)) * 30
    score += (len(set(x) & set(y)) / len(set(x + y))) * 50
    return score


def find_word(message):
    cleanse = lambda x: ''.join(y for y in x if y.isalpha())
    average = lambda x: sum(x) / len(x)
    words = list(map(cleanse, message.lower().split(' ')))
    scores = {x: [] for x in words}
    for x, y in itertools.combinations(words, 2):
        score = calc_coefficient(x, y)
        scores[x].append(score)
        scores[y].append(score)
    return sorted({w: average(l) for w, l in scores.items()}.items(), key=lambda x: (x[1], words.index(x[0])), reverse=True)[0][0]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_word("Speak friend and enter.") == "friend", "Friend"
    assert find_word("Beard and Bread") == "bread", "Bread is Beard"
    assert find_word("The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     "I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word("Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     " According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word("One, two, two, three, three, three.") == "three", "Repeating"
