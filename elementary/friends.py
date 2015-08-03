import itertools


class Friends:
    def __init__(self, connections):
        self.connections = connections

    def add(self, connection):
        if connection in self.connections:
            return False
        self.connections = self.connections + (connection,)
        return True

    def remove(self, connection):
        if connection not in self.connections:
            return False
        self.connections = tuple(x for x in self.connections if x != connection)
        return True

    def names(self):
        return set(itertools.chain(*self.connections))

    def connected(self, name):
        result = set(itertools.chain(*[x for x in self.connections if name in x]))
        result.remove(name)
        return result if result else set()


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
