#!/usr/bin/env python3

with open("input.txt") as f:
    memory = list(map(int, f.read().split(",")))


class IntcodeComputer(object):
    def __init__(self, memory, inputs):
        self.memory = memory + [0] * 100000000
        self.inputs = inputs

        self.pos = 0
        self.inputs_ind = 0
        self.relative_base = 0
        self.exit_code = 0
        self.diagnostic_code = 0
        self.has_new_output = False

    def get_param(self, offset, mode):
        if mode == 0:  # position mode
            return self.memory[self.memory[self.pos + offset]]
        elif mode == 1:  # immediate mode
            return self.memory[self.pos + offset]
        elif mode == 2:  # relative mode
            return self.memory[self.memory[self.pos + offset] + self.relative_base]

    def assign(self, value, pos_index, mode):
        if mode == 0:  # position mode
            self.memory[self.memory[pos_index]] = value
        elif mode == 2:  # relative mode
            self.memory[self.memory[pos_index] + self.relative_base] = value

    def step(self, with_logging):
        instruction = str(self.memory[self.pos]).zfill(5)
        opcode = instruction[-2:]
        modes = list(map(int, instruction[:3]))

        if opcode == "03":  # input
            assert modes[2] in [0, 2]
            self.assign(self.inputs[self.inputs_ind], self.pos + 1, modes[2])
            self.inputs_ind += 1
            self.pos += 2
        elif opcode == "02" or opcode == "01":
            arg1 = self.get_param(1, modes[2])
            arg2 = self.get_param(2, modes[1])
            assert modes[0] in [0, 2]
            if opcode == "02":  # multiply
                self.assign(arg1 * arg2, self.pos + 3, modes[0])
            elif opcode == "01":  # add
                self.assign(arg1 + arg2, self.pos + 3, modes[0])
            self.pos += 4
        elif opcode == "04":  # output
            self.diagnostic_code = self.get_param(1, modes[2])
            self.has_new_output = True
            if with_logging:
                print("Output:", self.diagnostic_code)
            self.pos += 2
        elif opcode == "05":  # jump if true
            arg1 = self.get_param(1, modes[2])
            arg2 = self.get_param(2, modes[1])
            if arg1 != 0:
                self.pos = arg2
            else:
                self.pos += 3
        elif opcode == "06":  # jump if false
            arg1 = self.get_param(1, modes[2])
            arg2 = self.get_param(2, modes[1])
            if arg1 == 0:
                self.pos = arg2
            else:
                self.pos += 3
        elif opcode == "07":  # less than
            arg1 = self.get_param(1, modes[2])
            arg2 = self.get_param(2, modes[1])
            self.assign(1 if arg1 < arg2 else 0, self.pos + 3, modes[0])
            self.pos += 4
        elif opcode == "08":  # equals
            arg1 = self.get_param(1, modes[2])
            arg2 = self.get_param(2, modes[1])
            self.assign(1 if arg1 == arg2 else 0, self.pos + 3, modes[0])
            self.pos += 4
        elif opcode == "09":  # adjust relative base
            arg1 = self.get_param(1, modes[2])
            self.relative_base += arg1
            self.pos += 2

    def run(self, with_logging=False):
        self.has_new_output = False
        while self.memory[self.pos] != 99 and not self.has_new_output:
            self.step(with_logging)
        return self.diagnostic_code


BLACK = 0
WHITE = 1

heading = 0  # 0 is up, increasing clockwise
x, y = 0, 0

colors = {}
colors[(x, y)] = WHITE
computer = IntcodeComputer(memory, [])
while computer.memory[computer.pos] != 99:
    computer.inputs.append(colors[(x, y)] if (x, y) in colors else BLACK)

    colors[(x, y)] = computer.run()
    direction_change = computer.run()

    if direction_change == 0:  # rotate left
        heading -= 1
    else:  # rotate right
        heading += 1
    heading %= 4

    if heading == 0:
        y -= 1
    elif heading == 1:
        x -= 1
    elif heading == 2:
        y += 1
    elif heading == 3:
        x += 1

min_x = min(c[0] for c in colors.keys())
max_x = max(c[0] for c in colors.keys())
min_y = min(c[1] for c in colors.keys())
max_y = max(c[1] for c in colors.keys())

for y in range(min_y, max_y + 1):
    row = [
        "*" if (x, y) in colors and colors[(x, y)] == WHITE else " "
        for x in range(max_x, min_x, -1)
    ]
    print("".join(row))
