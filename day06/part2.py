#!/usr/bin/env python3

from collections import deque, defaultdict

orbiters = {}
orbitees = defaultdict(set)
with open("input.txt") as f:
    for line in f:
        orbitee, orbiter = line.strip().split(')')
        orbiters[orbiter] = orbitee
        orbitees[orbitee].add(orbiter)

assert "SAN" in orbiters
assert "YOU" in orbiters

q = deque()
q.append(("SAN", 0))
visited = set()
while q:
    node, dist = q.popleft()
    visited.add(node)
    if node == "YOU":
        print(dist-2)
        exit()

    for orbitee in orbitees[node]:
        if orbitee in visited:
            continue
        q.append((orbitee, dist+1))
    if node in orbiters and orbiters[node] not in visited:
        q.append((orbiters[node], dist+1))
