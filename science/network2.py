def capture(matrix):
    reached, injected = {0}, {0}
    security_levels = [row[i] for i, row in enumerate(matrix)]
    connected = [[j for j, x in enumerate(row) if x and i != j] for i, row in enumerate(matrix)]
    time = 0
    while True:
        reached.update(x for x in range(len(matrix)) if len([y for y in connected[x] if y in injected]))
        # attack
        for i in reached:
            security_levels[i] -= 1 if security_levels[i] > 0 else 0
        injected.update(i for i, x in enumerate(security_levels) if x == 0)
        time += 1
        if len(injected) == len(matrix):
            return time


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"
