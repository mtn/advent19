#!/usr/bin/env python3

total = 0
with open("input.txt") as f:
    for line in f:
        total += int(line.strip()) // 3 - 2

print(total)
