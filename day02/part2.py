#!/usr/bin/env python3

import copy

with open("input.txt") as f:
    memory = list(map(int, f.read().split(",")))

for noun in range(100):
    for verb in range(100):
        mem = copy.deepcopy(memory)
        mem[1] = noun
        mem[2] = verb
        pos = 0
        while mem[pos] != 99:
            if mem[pos] == 1:
                mem[mem[pos + 3]] = mem[memory[pos + 1]] + mem[mem[pos + 2]]
            elif memory[pos] == 2:
                mem[mem[pos + 3]] = mem[memory[pos + 1]] * mem[mem[pos + 2]]
            pos += 4

        if mem[0] == 19690720:
            print(100 * noun + verb)
