from IntcodeComputer import IntcodeComputer
from copy import deepcopy
import os
import sys
sys.setrecursionlimit(1000000000)


def createMem(str): return list(map(int, str.strip("\n").split(",")))


f = open("aoc15.txt", "r")


NOPOSCHANGE, PROGRESSING, DONE = 0, 1, 2

fewest_steps = float("inf")
machine = IntcodeComputer(createMem(f.readline()))
most_steps = float("-inf")


coordincs = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}


def run(currmachine, visited, coords, doneFound=False):
    def dooby(i, currmem, curroutput):
        global fewest_steps
        global most_steps
        currmachine.run([i])
        last_output = currmachine.output[-1]
        if last_output == NOPOSCHANGE:
            if doneFound:
                most_steps = max(most_steps, len(currmachine.output))
        elif last_output == PROGRESSING:
            coordinc = coordincs[i]
            run(currmachine, visited,
                (coords[0]+coordincs[i][0], coords[1]+coordincs[i][1]))
        elif last_output == DONE and not doneFound:
            print("fk")
            fewest_steps = min(fewest_steps, len(currmachine.output))
            currmachine.output.clear()
            run(deepcopy(currmachine), set(), coords, True)

    #print(coords, doneFound)
    if coords in visited:
        return
    visited.add(coords)
    for i in range(1, 5):
        dooby(i, currmachine.mem[:], currmachine.output[:])

    visited.remove(coords)


print("running")
run(machine, set(), (0, 0))
print("fewest_steps: ", fewest_steps)
print("most_steps: ", most_steps)
print("done")
