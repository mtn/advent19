#!/usr/bin/env python3

import copy
import numpy as np

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


def get_steps_till_repeat(moons):
    positions, velocities = moons
    original_moons = copy.deepcopy(moons)
    step = 0

    while not step or [positions, velocities] != original_moons:
        for i, p1 in enumerate(positions):
            for j, p2 in enumerate(positions):
                if p1 == p2:
                    continue
                velocities[i] += 1 if p1 < p2 else -1

        for i in range(len(positions)):
            positions[i] += velocities[i]

        step += 1

    return step

xs = [m[0][0] for m in moons]
ys = [m[0][1] for m in moons]
zs = [m[0][2] for m in moons]

x_steps = get_steps_till_repeat([xs, [0]*len(xs)])
y_steps = get_steps_till_repeat([ys, [0]*len(xs)])
z_steps = get_steps_till_repeat([zs, [0]*len(xs)])

print(np.lcm(np.lcm(x_steps, y_steps), z_steps))
