import os
from IntcodeComputer import IntcodeComputer


def createMem(str): return list(map(int, str.strip("\n").split(",")))


f = open("aoc14.txt", "r")

machine = IntcodeComputer(createMem(f.readline()))
while(not machine.halted):
    machine.run()
