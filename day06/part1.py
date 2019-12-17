#!/usr/bin/env python3

from collections import deque, defaultdict

orbiters = {}
orbitees = defaultdict(set)
with open("input.txt") as f:
    for line in f:
        orbitee, orbiter = line.strip().split(')')
        orbiters[orbiter] = orbitee
        orbitees[orbitee].add(orbiter)

# find the root
for n in orbiters.values():
    if n not in orbiters.keys():
        root = n

total = 0
q = deque()
q.append((root, 1))
while q:
    node, dist = q.popleft()
    for orbitee in orbitees[node]:
        total += dist
        q.append((orbitee, dist+1))

print(total)
