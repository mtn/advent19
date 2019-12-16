#!/usr/bin/env python3

inp = "357253-892942"
low, high = map(int, inp.split("-"))


def meets_criteria(i):
    has_adjacent = False
    decreases = False
    for l, r in zip(str(i), str(i)[1:]):
        if l == r:
            has_adjacent = True
        if int(l) > int(r):
            decreases = True

    return has_adjacent and not decreases

total = 0
for i in range(low, high+1):
    total += meets_criteria(i)
print(total)
