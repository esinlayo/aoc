import os
from IntcodeComputer import IntcodeComputer


def createMem(str): return list(map(int, str.strip("\n").split(",")))


f = open("aoc21.txt", "r")

machine = IntcodeComputer(createMem(f.readline()))
instr = ""
'''
"NOT C T", "AND D T", "AND G T", "NOT A J", "OR T J",
"NOT C T", "AND D T", "AND H T",
"OR T J"
'''
'''
    "NOT C T", "AND D T", "AND G J", "OR H J", "AND T J",
    "NOT A T",
    "OR T J"
'''
for n in (
    #"NOT C T", "AND D T", "AND G T", "NOT C J", "AND D J", "AND H J", "OR J T", "NOT A J", "OR T J"
    "AND G T", "OR H T", "NOT C J", "AND D J", "AND J T", "NOT A J", "OR T J"
):
    instr += n
    instr += "\n"
instr += "RUN\n"

machine.inputQ.extend([ord(char) for char in instr])
while(not machine.halted):
    machine.run()

for e in machine.output:
    print(chr(e), end='')
