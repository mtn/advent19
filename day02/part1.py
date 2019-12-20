#!/usr/bin/env python3

with open("input.txt") as f:
    memory = list(map(int, f.read().split(",")))

memory[1] = 12
memory[2] = 2

pos = 0
while memory[pos] != 99:
    if memory[pos] == 1:
        memory[memory[pos + 3]] = memory[memory[pos + 1]] + memory[memory[pos + 2]]
    elif memory[pos] == 2:
        memory[memory[pos + 3]] = memory[memory[pos + 1]] * memory[memory[pos + 2]]
    pos += 4

print(memory[0])
