#!/usr/bin/env python3


with open("input.txt") as f:
    memory = list(map(int, f.read().split(',')))
    inputs = [5]

class IntcodeComputer(object):
    def __init__(self, memory, inputs):
        self.memory = memory
        self.inputs = inputs

        self.pos = 0
        self.inputs_ind = 0
        self.exit_code = 0
        self.diagnostic_code = 0

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
            output = self.get_param(1, modes[2])
            if with_logging:
                print("Output:", output, self.pos)
            self.pos += 2
            if output != 0:
                if self.memory[self.pos] == 99:
                    self.exit_code = 0
                    self.diagnostic_code = output
                else:
                    self.exit_code = 1
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
        while self.memory[self.pos] != 99 and self.exit_code == 0:
            self.step(with_logging)

computer = IntcodeComputer(memory, inputs)
# computer.run(with_logging=True)
computer.run()
assert computer.exit_code == 0
print(computer.diagnostic_code)
