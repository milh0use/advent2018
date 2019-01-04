# Advent of Code 2018 Day 16
#
#
#

file = open("Advent16.txt", 'r')

# Extract inputs

inputEOF = False
input_phase = 1
tests = []
codes = []
while not inputEOF:
    while input_phase == 1:
        try:
            before = next(file).rstrip("\n")
            if "Before" not in before:
                next(file)
                input_phase = 2
                break
            before = list(map(int, before[9:19].split(", ")))
            code = list(map(int, next(file).rstrip("\n").split(" ")))
            after = list(map(int, next(file).rstrip("\n")[9:19].split(", ")))

            next(file)
            tests.append([before, code, after])
        except StopIteration:
            inputEOF = True
            input_phase = False
            break

    while input_phase == 2:
        try:
            codes.append(list(map(int, next(file).rstrip("\n").split(" "))))
        except StopIteration:
            inputEOF = True
            input_phase = False
            break


class Registers(object):

    def __init__(self, values):
        self.registers = values[:]
        self.opcode = None
        self.inputA = None
        self.inputB = None
        self.output = None

    #
    # Addition:
    # addr (add register) stores into register C the result of adding register A and register B.
    def addr(self, opcode, inputA, inputB, outputC):
        self.opcode = opcode
        self.inputA = inputA
        self.inputB = inputB
        self.output = outputC
        self.registers[self.output] = self.registers[self.inputA] + self.registers[self.inputB]
        return

    # addi (add immediate) stores into register C the result of adding register A and value B.
    def addi(self, opcode, inputA, inputB, outputC):
        self.opcode = opcode
        self.inputA = inputA
        self.inputB = inputB
        self.output = outputC
        self.registers[self.output] = self.registers[self.inputA] + self.inputB
        return

    #
    # Multiplication:
    # mulr (multiply register) stores into register C the result of multiplying register A and register B.
    def mulr(self, opcode, inputA, inputB, outputC):
        self.opcode = opcode
        self.inputA = inputA
        self.inputB = inputB
        self.output = outputC
        self.registers[self.output] = self.registers[self.inputA] * self.registers[self.inputB]
        return

    # muli (multiply immediate) stores into register C the result of multiplying register A and value B.
    def muli(self, opcode, inputA, inputB, outputC):
        self.opcode = opcode
        self.inputA = inputA
        self.inputB = inputB
        self.output = outputC
        self.registers[self.output] = self.registers[self.inputA] * self.inputB
        return

    #
    # Bitwise AND:
    # banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
    def banr(self, opcode, inputA, inputB, outputC):
        self.opcode = opcode
        self.inputA = inputA
        self.inputB = inputB
        self.output = outputC
        self.registers[self.output] = self.registers[self.inputA] & self.registers[self.inputB]
        return

    # bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
    def bani(self, opcode, inputA, inputB, outputC):
        self.opcode = opcode
        self.inputA = inputA
        self.inputB = inputB
        self.output = outputC
        self.registers[self.output] = self.registers[self.inputA] & self.inputB
        return

    #
    # Bitwise OR:
    # borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
    def borr(self, opcode, inputA, inputB, outputC):
        self.opcode = opcode
        self.inputA = inputA
        self.inputB = inputB
        self.output = outputC
        self.registers[self.output] = self.registers[self.inputA] | self.registers[self.inputB]
        return

    # bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
    def bori(self, opcode, inputA, inputB, outputC):
        self.opcode = opcode
        self.inputA = inputA
        self.inputB = inputB
        self.output = outputC
        self.registers[self.output] = self.registers[self.inputA] | self.inputB

    #
    # Assignment:
    # setr (set register) copies the contents of register A into register C. (Input B is ignored.)
    def setr(self, opcode, inputA, inputB, outputC):
        self.opcode = opcode
        self.inputA = inputA
        self.inputB = inputB
        self.output = outputC
        self.registers[self.output] = self.registers[self.inputA]
        return

    # seti (set immediate) stores value A into register C. (Input B is ignored.)
    def seti(self, opcode, inputA, inputB, outputC):
        self.opcode = opcode
        self.inputA = inputA
        self.inputB = inputB
        self.output = outputC
        self.registers[self.output] = self.inputA
        return

    #
    # Greater-than testing:
    # gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
    def gtir(self, opcode, inputA, inputB, outputC):
        self.opcode = opcode
        self.inputA = inputA
        self.inputB = inputB
        self.output = outputC
        self.registers[self.output] = 1 if self.inputA > self.registers[self.inputB] else 0
        return

    # gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
    def gtri(self, opcode, inputA, inputB, outputC):
        self.opcode = opcode
        self.inputA = inputA
        self.inputB = inputB
        self.output = outputC
        self.registers[self.output] = 1 if self.registers[self.inputA] > self.inputB else 0

    # gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
    def gtrr(self, opcode, inputA, inputB, outputC):
        self.opcode = opcode
        self.inputA = inputA
        self.inputB = inputB
        self.output = outputC
        self.registers[self.output] = 1 if self.registers[self.inputA] > self.registers[self.inputB] else 0

    #
    # Equality testing:
    # eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
    def eqir(self, opcode, inputA, inputB, outputC):
        self.opcode = opcode
        self.inputA = inputA
        self.inputB = inputB
        self.output = outputC
        self.registers[self.output] = 1 if self.inputA == self.registers[self.inputB] else 0

        return

    # eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
    def eqri(self, opcode, inputA, inputB, outputC):
        self.opcode = opcode
        self.inputA = inputA
        self.inputB = inputB
        self.output = outputC
        self.registers[self.output] = 1 if self.registers[self.inputA] == self.inputB else 0

    # eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
    def eqrr(self, opcode, inputA, inputB, outputC):
        self.opcode = opcode
        self.inputA = inputA
        self.inputB = inputB
        self.output = outputC
        self.registers[self.output] = 1 if self.registers[self.inputA] == self.registers[self.inputB] else 0


commands = ["addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori", "setr", "seti", "gtir", "gtri", "gtrr",
            "eqir", "eqri", "eqrr"]
success = []
success_count = []
for reg, code, out in tests:

    opcode, inputA, inputB, outputC = code
    success_row = []
    for command in commands:
        x = Registers(reg)
        exec("x.{}(opcode, inputA, inputB, outputC)".format(command))
        success_row.append(reg == x.registers)
    success.append(success_row)
    success_count.append(sum(success_row))
    break  # Advent of Code 2018 Day 16
#
#
#

file = open("Advent16.txt", 'r')

# Extract inputs

inputEOF = False
input_phase = 1
tests = []
codes = []
while not inputEOF:
    while input_phase == 1:
        try:
            before = next(file).rstrip("\n")
            if "Before" not in before:
                next(file)
                input_phase = 2
                break
            before = list(map(int, before[9:19].split(", ")))
            code = list(map(int, next(file).rstrip("\n").split(" ")))
            after = list(map(int, next(file).rstrip("\n")[9:19].split(", ")))

            next(file)
            tests.append([before, code, after])
        except StopIteration:
            inputEOF = True
            input_phase = False
            break

    while input_phase == 2:
        try:
            codes.append(list(map(int, next(file).rstrip("\n").split(" "))))
        except StopIteration:
            inputEOF = True
            input_phase = False
            break


commands = ["addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori", "setr", "seti", "gtir", "gtri", "gtrr",
            "eqir", "eqri", "eqrr"]
success = []
success_count = []
for reg, code, out in tests:

    opcode, inputA, inputB, outputC = code
    success_row = []
    for command in commands:
        x = Registers(reg)
        exec("x.{}(opcode, inputA, inputB, outputC)".format(command))
        success_row.append(out == x.registers)
    #       print(command, reg, code, x.registers, out == x.registers)
    success.append(success_row)
    success_count.append(sum(success_row))


print("Part 1: Tests with three or more possible commands", len([x for x in success_count if x >= 3]))
