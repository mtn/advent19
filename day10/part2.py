#!/usr/bin/env python3

import math

asteroids = []
with open("input.txt") as f:
    for line in f:
        asteroids.append(list(line.strip()))


def angle(a, b):
    ang = math.atan2(b[0] - a[0], a[1] - b[1]) * 180 / math.pi
    return ang + 360 if ang < 0 else ang


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

            angles.add(angle((x, y), (rx, ry)))
    return len(angles)


max_visible = 0
best_x, best_y = 0, 0
for (ry, row) in enumerate(asteroids):
    for (rx, col) in enumerate(row):
        visible = num_visible(rx, ry)
        if visible > max_visible:
            max_visible = visible
            best_x, best_y = rx, ry

to_vaporize = 200
vapq = []
for (ry, row) in enumerate(asteroids):
    for (rx, col) in enumerate(row):
        if asteroids[ry][rx] == "." or (rx == best_x and ry == best_y):
            continue

        vapq.append((angle((best_x, best_y), (rx, ry)), (rx, ry)))

vapq.sort(key=lambda x: (x[0], abs(best_x - x[1][0]) + abs(best_y - x[1][1])))

last_angle = None
num_vaporized = 0
ind = 0

while num_vaporized != 200:
    if ind >= len(vapq):
        ind = 0
        last_angle = None

    angle, (rx, ry) = vapq[ind]

    if last_angle is None or angle != last_angle:
        last_angle = angle
        last_popped = vapq.pop(ind)
        num_vaporized += 1
    else:
        ind += 1

_, (last_x, last_y) = last_popped
print(100 * last_x + last_y)
