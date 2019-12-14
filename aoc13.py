import os
from IntcodeComputer import IntcodeComputer


def createMem(str): return list(map(int, str.strip("\n").split(",")))


f = open("aoc13.txt", "r")

pics = {0: ' ', 1: 'X', 2: '.', 3: 'P', 4: 'o'}


def printGame():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(machine.currentScore)
    for i, row in enumerate(game):
        print(f'{i:02} ', end='')
        for x in row:
            print(pics.get(x, ' '), end='')
        print()


game = [[' ' for _ in range(41)] for _ in range(25)]
machine = IntcodeComputer(createMem(f.readline()))
blocktiles = 0
total = 0
while(not machine.halted):
    machine.run()
    machine.run()
    machine.run()

    if machine.output:
        x, y, sprite = machine.output
        game[y][x] = sprite

        if sprite == 3:
            print("paddle init: ", (x, y))          # (20, 23)

        blocktiles += 1 if machine.output[2] == 2 else 0
        machine.output.clear()

print(blocktiles)


f = open("aoc13.txt", "r")
machine = IntcodeComputer(createMem(f.readline()))
machine.mem[0] = 2

currentScore = None
ball_xpos, paddle_xpos = None, 20

print()
while(not machine.halted):
    machine.run()
    machine.run()
    machine.run()

    if machine.output and len(machine.output) == 3:
        if machine.output[2] == 4:          # Info about the ball
            ball_xpos = machine.output[0]

            if paddle_xpos < ball_xpos:
                machine.inputQ.extend([1])
                paddle_xpos += 1
            elif paddle_xpos > ball_xpos:
                machine.inputQ.extend([-1])
                paddle_xpos -= 1
            else:
                machine.inputQ.extend([0])

        if machine.output[:2] == [-1, 0]:   # Info about current score
            currentScore = machine.output[2]

        machine.output.clear()
print("score", currentScore)
