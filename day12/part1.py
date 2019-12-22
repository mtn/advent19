#!/usr/bin/env python3

import itertools

STEPS = 1000

moons = []
with open("input.txt") as f:
    for line in f:
        line = line.strip().split("=")
        x = int(line[1].split(",")[0])
        y = int(line[2].split(",")[0])
        z = int(line[-1][:-1])

        moons.append([[x, y, z], [0, 0, 0]])

def update_velocity(ind, m1, m2):
    if m1[0][ind] > m2[0][ind]:
        m1[1][ind] -= 0.5
        m2[1][ind] += 0.5
    elif m1[0][ind] < m2[0][ind]:
        m1[1][ind] += 0.5
        m2[1][ind] -= 0.5

def print_status(step):
    print(f"After {step} steps:")
    for m in moons:
        pos = f"pos=<x={m[0][0]}, y={m[0][1]}, z={m[0][2]}>"
        vel = f"vel=<x={m[1][0]}, y={m[1][1]}, z={m[1][2]}>"
        print(pos + " " + vel)
    print("")


# print_status(0)
for step in range(STEPS):
    for (m1, m2) in itertools.product(moons, moons):
        if m1 == m2:
            continue

        update_velocity(0, m1, m2)
        update_velocity(1, m1, m2)
        update_velocity(2, m1, m2)

    for m in moons:
        for i in range(3):
            m[0][i] += m[1][i]

    # print_status(step+1)

energy = 0
for m in moons:
    energy += sum(map(abs, m[0])) * sum(map(abs, m[1]))
print(int(energy))
