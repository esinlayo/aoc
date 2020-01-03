import os
from IntcodeComputer import IntcodeComputer


def createMem(str): return list(map(int, str.strip("\n").split(",")))


f = open("aoc19.txt", "r")
mem = createMem(f.readline())


inputs = []
for r in range(50):
    for c in range(50):
        inputs.append((r, c))


# print(inputs)
outputs = []
outsmol = []
for i in inputs:
    machine = IntcodeComputer(mem, list(i))
    while(not machine.halted):
        machine.run()
    outsmol.extend(machine.output[:])
    if len(outsmol) == 50:
        outputs.append(outsmol[:])
        outsmol.clear()

cnt = 0
img = {0: '.', 1: '#'}

' TODO : STUDY X AND Y MADNESS AND MAKE A STRAT FOR PROCESSING MATRIC TO GET ROTATION '

for i in range(50):
    print(i % 10, end='')
for r, row in enumerate(outputs):
    print(row)

for r in range(len(outputs)):
    for c in range(len(outputs[r])):
        print(img[outputs[r][c]], end='')
    print()


print(cnt)
