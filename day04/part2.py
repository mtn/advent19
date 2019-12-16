#!/usr/bin/env python3

inp = "357253-892942"
low, high = map(int, inp.split("-"))


def meets_criteria(i):
    has_adjacent = False
    decreases = False
    inp = str(i)
    for l in range(5):
        if inp[l] == inp[l+1] and (l == 0 or inp[l-1] != inp[l]) and (l==4 or inp[l+2] != inp[l]):
            has_adjacent = True
        if int(inp[l]) > int(inp[l+1]):
            decreases = True

    return has_adjacent and not decreases

total = 0
for i in range(low, high+1):
    total += meets_criteria(i)
print(total)
