from IntcodeComputer import IntcodeComputer
import os
import sys
sys.setrecursionlimit(1000000000)


def createMem(str): return list(map(int, str.strip("\n").split(",")))


f = open("aoc15.txt", "r")


NOPOSCHANGE, PROGRESSING, DONE = 0, 1, 2

fewest_steps = float("inf")
machine = IntcodeComputer(createMem(f.readline()))


def run(currmachine, visited, coords, doneFound=False):
    global fewest_steps
    #print(f"running {currmachine} {coords}")
    if coords in visited:
        return
    visited.add(coords)

    currmem = currmachine.mem[:]
    curroutput = currmachine.output[:]

    currmachine.mem, currmachine.output = currmem[:], curroutput[:]
    currmachine.run([1])
    last_output = currmachine.output[-1]
    if last_output == NOPOSCHANGE:
        pass
    elif last_output == PROGRESSING:
        run(currmachine, visited, (coords[0], coords[1]+1))
    elif last_output == DONE and not doneFound:
        print(len(currmachine.output))
        fewest_steps = min(fewest_steps, len(currmachine.output))

    currmachine.mem, currmachine.output = currmem[:], curroutput[:]
    currmachine.run([2])
    last_output = currmachine.output[-1]
    # print(last_output)
    if last_output == NOPOSCHANGE:
        pass
    elif last_output == PROGRESSING:
        run(currmachine, visited, (coords[0], coords[1]-1))
    elif last_output == DONE and not doneFound:
        print(len(currmachine.output))
        fewest_steps = min(fewest_steps, len(currmachine.output))

    currmachine.mem, currmachine.output = currmem[:], curroutput[:]
    currmachine.run([3])
    last_output = currmachine.output[-1]
    if last_output == NOPOSCHANGE:
        pass
    elif last_output == PROGRESSING:
        run(currmachine, visited, (coords[0]-1, coords[1]))
    elif last_output == DONE and not doneFound:
        print(len(currmachine.output))
        fewest_steps = min(fewest_steps, len(currmachine.output))

    currmachine.mem, currmachine.output = currmem[:], curroutput[:]
    currmachine.run([4])
    last_output = currmachine.output[-1]
    if last_output == NOPOSCHANGE:
        pass
    elif last_output == PROGRESSING:
        run(currmachine, visited, (coords[0]+1, coords[1]))
    elif last_output == DONE and not doneFound:
        print(len(currmachine.output))
        fewest_steps = min(fewest_steps, len(currmachine.output))

    visited.remove(coords)


visited = set()
print("running")
run(machine, visited, (0, 0))
print("fewest_steps: ", fewest_steps)
print("done")
