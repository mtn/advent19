#!/usr/bin/env python3

def getpts(path):
    pts = dict()
    loc = [0, 0]

    steps_taken = 0
    for step in path:
        direction = step[0]
        distance = int(step[1:])

        if direction == 'R':
            for s in range(distance):
                steps_taken += 1
                new_loc = (loc[0] + s + 1, loc[1])
                if new_loc in pts:
                    continue
                pts[new_loc] = steps_taken
            loc[0] += distance
        elif direction == 'L':
            for s in range(distance):
                steps_taken += 1
                new_loc = (loc[0] - s - 1, loc[1])
                if new_loc in pts:
                    continue
                pts[new_loc] = steps_taken
            loc[0] -= distance
        elif direction == 'U':
            for s in range(distance):
                steps_taken += 1
                new_loc = (loc[0], loc[1] - s - 1)
                if new_loc in pts:
                    continue
                pts[new_loc] = steps_taken
            loc[1] -= distance
        elif direction == 'D':
            for s in range(distance):
                steps_taken += 1
                new_loc = (loc[0], loc[1] + s + 1)
                if new_loc in pts:
                    continue
                pts[new_loc] = steps_taken
            loc[1] += distance

    return pts

with open("input.txt") as f:
    directions = f.read()
    path1, path2 = map(lambda x: x.split(','), directions.strip().split('\n'))

pts1 = getpts(path1)
pts2 = getpts(path2)

intersections = set(pts1.keys()).intersection(set(pts2.keys()))

min_steps = None
closest = None
for i in intersections:
    steps_taken = pts1[i] + pts2[i]
    if min_steps is None or steps_taken < min_steps:
        closest = i
        min_steps = steps_taken

print(min_steps)
