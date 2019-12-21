#!/usr/bin/env python3

import math

asteroids = []
with open("input.txt") as f:
    for line in f:
        asteroids.append(list(line.strip()))


def num_visible(x, y):
    if asteroids[y][x] == ".":
        return 0

    angles = set()
    for (ry, row) in enumerate(asteroids):
        for (rx, col) in enumerate(row):
            if rx == x and ry == y or asteroids[ry][rx] != "#":
                continue

            dx = x - rx
            dy = y - ry

            angles.add(math.atan2(dy, dx))

    return len(angles)


max_visible = 0
best_x, best_y = 0, 0
for (ry, row) in enumerate(asteroids):
    for (rx, col) in enumerate(row):
        visible = num_visible(rx, ry)
        if visible > max_visible:
            max_visible = visible
            best_x, best_y = rx, ry

print(max_visible)
