#!/usr/bin/env python3

def calculate_fuel(mass):
    t = 0
    mass = mass // 3 - 2
    while mass > 0:
        t += mass
        mass = mass // 3 - 2

    return t

total = 0

with open("input.txt") as f:
    for line in f:
        total += calculate_fuel(int(line.strip()))

print(total)
