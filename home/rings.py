import itertools


def break_rings(connections):
    remain_rings = lambda L: set(itertools.chain(*L))
    remain_links = lambda r, L: [x for x in L if r not in x]
    rings = remain_rings(connections)
    count = 0
    while True:
        rings_after_break, links_after_break = len(rings), len(connections)
        next_break = None
        for r in rings:
            check = len(remain_rings(remain_links(r, connections)))
            # break the ring that reduce number of rings best
            if check < rings_after_break:
                rings_after_break = check
                next_break = r
            # if there are rings that reduce same number,
            # break the most connected ring
            elif check == rings_after_break:
                check = len(remain_links(r, connections))
                if check < links_after_break:
                    links_after_break = check
                    next_break = r
        connections = remain_links(next_break, connections)
        rings = remain_rings(connections)
        count += 1
        if len(rings) == 0:
            break
    return count


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert break_rings(({1,9},{1,2},{8,5},{4,6},{5,6},{8,1},{3,4},{2,6},{9,6},{8,4},{8,3},{5,7},{9,7},{2,3},{1,7},)) == 5, "example"
    assert break_rings(({1,9},{1,2},{8,5},{4,6},{5,6},{8,1},{3,4},{2,6},{9,6},{8,4},{8,3},{5,7},{9,7},{2,3},{1,7},)) == 5, "All to all"
    assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
    assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"
    assert break_rings(({3,4},{5,6},{2,7},{1,5},{2,6},{8,4},{1,7},{4,5},{9,5},{2,3},{8,2},{2,4},{9,6},{5,7},{3,6},{1,3},)) == 5, "Long chain"
