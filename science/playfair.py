from string import ascii_lowercase as alpha, digits

TABLE_SIZE = 6


def prepare_message(message):
    filtered = [c for c in message.lower() if c.isalnum()]
    prepared = []
    while filtered:
        if len(filtered) != 1:
            a, b = filtered[0], filtered[1]
        else:
            a = filtered[0]
            b = 'z' if a != 'z' else 'x'
        filtered = filtered[2:]
        if a != b:
            prepared.append(a + b)
        else:
            x = 'x' if a != 'x' else 'z'
            prepared.append(a + x)
            filtered.insert(0, b)
    return prepared


def to_table(text, length):
    table, row = [], []
    for i, c in enumerate(text):
        if i % length:
            row.append(c)
        else:
            if row:
                table.append(row)
                row = []
            row.append(c)
    table.append(row[:length])
    return table


def encode(message, key):
    uniqualize = lambda L: ''.join(sorted(list(set(L)), key=lambda x: L.index(x)))
    key_table = to_table(uniqualize(uniqualize(key) + alpha + digits), TABLE_SIZE)
    prepared = prepare_message(message)
    import pdb;pdb.set_trace()


def decode(secret_message, key):
    return secret_message


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert encode("Fizz Buzz is x89 XX.", "checkio101") == 'do2y7mt22kry94y2y2', "Encode fizz buzz"
    # assert decode("do2y7mt22kry94y2y2", "checkio101") == 'fizxzbuzzisx89xzxz', "Decode fizz buzz"
    assert encode("How are you?", "hello") == 'ea2imb1ht0', "Encode How are you"
    # assert decode("ea2imb1ht0", "hello") == 'howareyouz', "Decode How are you"
    assert encode("My name is Alex!!!", "alexander") == 'i1dlkxjqlexn', "Encode Alex"
    # assert decode("i1dlkxjqlexn", "alexander") == 'mynameisalex', "Decode Alex"
    assert encode("Who are you?", "human") == 'rnvftc1jd5', "Encode WHo"
    # assert decode("rnvftc1jd5", "human") == 'whoareyouz', "Decode Who"
    assert encode("ATTACK AT DAWN", "general") == 'ewwektewhnua', "Encode attack"
    # assert decode("ewwektewhnua", "general") == 'attackatdawn', "Decode attack"
