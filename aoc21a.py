import os
from IntcodeComputer import IntcodeComputer


def createMem(str): return list(map(int, str.strip("\n").split(",")))


f = open("aoc21.txt", "r")

machine = IntcodeComputer(createMem(f.readline()))
instr = ""
for n in (
    "AND B T", "OR C T", "NOT D J", "OR J T", "NOT T T",
    "NOT A J",
    "OR T J"
):
    instr += n
    instr += "\n"
instr += "WALK\n"

machine.inputQ.extend([ord(char) for char in instr])
while(not machine.halted):
    machine.run()

print(machine.output)
