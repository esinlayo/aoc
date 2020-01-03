import os
from IntcodeComputer import IntcodeComputer


def createMem(str): return list(map(int, str.strip("\n").split(",")))


f = open("aoc19.txt", "r")
mem = createMem(f.readline())

sz = 3

inputs = []
r, c = 5, 0
while True:
    r, c = r+1, c+1
    machine = IntcodeComputer(mem, list((r, c)))
    while(not machine.halted):
        machine.run()
    outputs = machine.output[:]
    while(outputs != [1]):
        print('ayy', r, c)
        c += 1
        mac = IntcodeComputer(mem, list((r, c)))
        while(not mac.halted):
            mac.run()
        outputs = mac.output[:]

    machine = IntcodeComputer(mem, list((r-(sz-1), c)))
    while(not machine.halted):
        machine.run()
    if machine.output != [1]:
        continue
    #print(r, c, "2")
    machine = IntcodeComputer(mem, list((r-(sz-1), c+(sz-1))))
    while(not machine.halted):
        machine.run()
    if machine.output != [1]:
        continue
    print(r, c)
    print((r-(sz-1))*10000 + c)
    break


'''
machine = IntcodeComputer(mem, list(i))
while(not machine.halted):
    machine.run()
outsmol.extend(machine.output[:])

img = {0: '.', 1: '#'}

'''
