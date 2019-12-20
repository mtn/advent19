#!/usr/bin/env python3


def getpts(path):
    pts = set()
    loc = [0, 0]

    for step in path:
        direction = step[0]
        distance = int(step[1:])

        if direction == "R":
            for s in range(distance):
                pts.add((loc[0] + s + 1, loc[1]))
            loc[0] += distance
        elif direction == "L":
            for s in range(distance):
                pts.add((loc[0] - s - 1, loc[1]))
            loc[0] -= distance
        elif direction == "U":
            for s in range(distance):
                pts.add((loc[0], loc[1] - s - 1))
            loc[1] -= distance
        elif direction == "D":
            for s in range(distance):
                pts.add((loc[0], loc[1] + s + 1))
            loc[1] += distance

    return pts


with open("input.txt") as f:
    directions = f.read()
    path1, path2 = map(lambda x: x.split(","), directions.strip().split("\n"))

pts1 = getpts(path1)
pts2 = getpts(path2)

intersections = pts1.intersection(pts2)

min_dist = None
closest = None
for i in intersections:
    dist = abs(i[0]) + abs(i[1])
    if min_dist is None or dist < min_dist:
        closest = i
        min_dist = dist

print(min_dist)
