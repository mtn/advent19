#!/usr/bin/env python3

import itertools

with open("input.txt") as f:
    memory = list(map(int, f.read().split(',')))

class IntcodeComputer(object):
    def __init__(self, memory, inputs):
        self.memory = memory
        self.inputs = inputs

        self.pos = 0
        self.inputs_ind = 0
        self.exit_code = 0
        self.diagnostic_code = 0
        self.has_new_output = False

    def get_param(self, offset, mode):
        if mode == 0: # position mode
            return self.memory[self.memory[self.pos+offset]]
        elif mode == 1: # immediate mode
            return self.memory[self.pos+offset]

    def step(self, with_logging):
        instruction = str(self.memory[self.pos]).zfill(5)
        opcode = instruction[-2:]
        modes = list(map(int, instruction[:3]))

        if opcode == '03': # input
            assert modes[2] == 0
            self.memory[self.memory[self.pos+1]] = self.inputs[self.inputs_ind]
            self.inputs_ind += 1
            self.pos += 2
        elif opcode == '02' or opcode == '01':
            arg1 = self.get_param(1, modes[2])
            arg2 = self.get_param(2, modes[1])
            assert modes[0] == 0
            if opcode == '02': # multiply
                self.memory[self.memory[self.pos+3]] = arg1 * arg2
            elif opcode == '01': # add
                self.memory[self.memory[self.pos+3]] = arg1 + arg2
            self.pos += 4
        elif opcode == '04': # output
            self.diagnostic_code = self.get_param(1, modes[2])
            self.has_new_output = True
            if with_logging:
                print("Output:", self.diagnostic_code, self.pos)
            self.pos += 2
        elif opcode == '05': # jump if true
            arg1 = self.get_param(1, modes[2])
            arg2 = self.get_param(2, modes[1])
            if arg1 != 0:
                self.pos = arg2
            else:
                self.pos += 3
        elif opcode == '06': # jump if false
            arg1 = self.get_param(1, modes[2])
            arg2 = self.get_param(2, modes[1])
            if arg1 == 0:
                self.pos = arg2
            else:
                self.pos += 3
        elif opcode == '07': # less than
            arg1 = self.get_param(1, modes[2])
            arg2 = self.get_param(2, modes[1])
            self.memory[self.memory[self.pos+3]] = 1 if arg1 < arg2 else 0
            self.pos += 4
        elif opcode == '08': # equals
            arg1 = self.get_param(1, modes[2])
            arg2 = self.get_param(2, modes[1])
            self.memory[self.memory[self.pos+3]] = 1 if arg1 == arg2 else 0
            self.pos += 4

    def run(self, with_logging=False):
        self.has_new_output = False
        while self.memory[self.pos] != 99 and not self.has_new_output:
            self.step(with_logging)

max_output = None
for phase_settings in itertools.permutations(range(5, 10)):
    second_input = 0
    computers = []
    # Run each computer once to properly initialize it
    for p in phase_settings:
        inputs = [p, second_input]
        computer = IntcodeComputer(list(memory), inputs)
        computers.append(computer)
        computer.run(with_logging=False)
        assert computer.exit_code == 0

        second_input = computer.diagnostic_code

    previous_output = second_input
    while not all(map(lambda x: x.memory[x.pos] == 99, computers)):
        for computer in computers:
            if not computer.memory[computer.pos] == 99:
                if previous_output is not None:
                    computer.inputs.append(previous_output)
                computer.run()
                if computer.has_new_output:
                    previous_output = computer.diagnostic_code
                else:
                    previous_output = None

    output = computers[-1].diagnostic_code

    if max_output is None or output > max_output:
        max_output = output

print(max_output)
