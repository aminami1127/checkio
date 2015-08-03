def golf(n):
    return [p for p in range(n+1,n+10000) if all(p % x for x in range(2,p)) and str(p)[::-1] == str(p)][0]


assert golf(2) == 3
assert golf(13) == 101
assert golf(101) == 131
