from IntcodeComputer import IntcodeComputer

'''
emergency hull painting robot

- move around on the grid of square panels on the side of your ship
- detect the color of its current panel
- and paint its current panel black or white.

- All panels currently black

The Intcode program will serve as the brain of the robot.
The program uses INPUT instructions to access the robot's camera:
    0 if the robot is over a black panel
    1 if the robot is over a white panel

Then, the program will output two values:
    First, it will output a value indicating the color to paint the panel the robot is over:
        0 means to paint the panel black, and 1 means to paint the panel white.

    Second, it will output a value indicating the direction the robot should turn:
        0 means it should turn left 90 degrees, and 1 means it should turn right 90 degrees.
'''


def createMem(str): return list(map(int, str.strip("\n").split(",")))


f = open("aoc11.txt", "r")

robot = IntcodeComputer(createMem(f.readline()))
robot.dir, robot.pos, robot.visited = 0, [0, 0], {}
increments = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
while (not robot.halted):
    robot.run([robot.visited.get(tuple(robot.pos), 0)])
    robot.run()

    if robot.output:
        robot.visited[tuple(robot.pos)] = robot.output[0]
        robot.dir += 1 if robot.output[1] == 1 else -1
        if robot.dir == 4:
            robot.dir = 0
        if robot.dir == -1:
            robot.dir = 3
        inc = increments[robot.dir]
        robot.pos = list([pos+inc[i] for i, pos in enumerate(robot.pos)])
        robot.output.clear()
# print(emergencyHullRobot.visited)
print("Part 1:", len(robot.visited))


print("---------------------------")
print("Part 2:")
f = open("aoc11.txt", "r")
robot = IntcodeComputer(createMem(f.readline()))
robot.dir, robot.pos, robot.visited = 0, [0, 0], {(0, 0): 1}
increments = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
while (not robot.halted):
    robot.run([robot.visited.get(tuple(robot.pos), 0)])
    robot.run()

    if robot.output:
        robot.visited[tuple(robot.pos)] = robot.output[0]
        robot.dir += 1 if robot.output[1] == 1 else -1
        if robot.dir == 4:
            robot.dir = 0
        if robot.dir == -1:
            robot.dir = 3
        inc = increments[robot.dir]
        robot.pos = list([pos+inc[i] for i, pos in enumerate(robot.pos)])
        robot.output.clear()


maxX, maxY = float("-inf"), float("-inf")
minX, minY = float("+inf"), float("+inf")
for coord, color in robot.visited.items():
    maxX = max(maxX, coord[0])
    minX = min(minX, coord[0])
    maxY = max(maxX, coord[1])
    minY = min(minY, coord[1])
Xlength = abs(minX)+abs(maxX)+1
Ylength = abs(minY)+abs(maxY)+1
print('X range', minX, maxX, 'X length', Xlength)
print('Y range', minY, maxY, 'Y length', Ylength)

print(abs(minX)+abs(maxX)+1, abs(minY)+abs(maxY)+1)
image = [[' ' for _ in range(Xlength)] for _ in range(Ylength)]

symbol = {0: '.', 1: '#'}

for coord, color in robot.visited.items():
    coordx, coordy = coord
    image[coordx+abs(minX)][coordy+abs(minY)] = symbol[color]

for row in image:
    for char in row:
        print(char, end='')
    print()
