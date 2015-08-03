def min(*args, **kwargs):
    key = kwargs.get("key", lambda x: x)
    values = iter(args[0]) if len(args) == 1 else iter(args)
    min_value = next(values)
    for i in values:
        if key(i) < key(min_value):
            min_value = i
    return min_value


def max(*args, **kwargs):
    key = kwargs.get("key", lambda x: x)
    values = iter(args[0]) if len(args) == 1 else iter(args)
    max_value = next(values)
    for i in values:
        if key(i) > key(max_value):
            max_value = i
    return max_value


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert max("hello") == "o", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
