from functools import reduce
from math import gcd

class Moon:
    def __init__(self, x, y, z):
        self.position, self.velocity = [x, y, z], [0,0,0]
        self.calcEnergy = lambda: sum(map(abs, self.position)) * sum(map(abs, self.velocity))

    def updateVelocity(self, other):
        for i, (selfpos, otherpos) in enumerate(zip(self.position, other.position)):
            if selfpos < otherpos: self.velocity[i] += 1
            elif selfpos > otherpos: self.velocity[i] -= 1

    def updatePosition(self):
        for i, (init, incr) in enumerate(zip(self.position, self.velocity)):
            self.position[i] = init + incr

            
#f = open("aoc12.txt", "r")
#x = f.readlines()
#x = list(filter(lambda x: len(x) > 0, map(lambda x: x.strip('\n<>'), x)))            
moons = [Moon(14,9,14), Moon(9,11,6), Moon(-6,14,-4), Moon(4,-4,-3)]
test = [Moon(-1,0,2), Moon(2,-10,-7), Moon(4,-8,8), Moon(3,5,-1)]

universe = set()
for _ in range(1000):
    for moon1 in moons:
        for moon2 in moons:
            if not moon1 is moon2: 
                moon1.updateVelocity(moon2)

    for moon in moons:
        moon.updatePosition()

energies = []
for moon in moons:
    energies.append(moon.calcEnergy())
print("Part 1:", sum(energies))
print("-------------------------------------------")

moons = [Moon(14,9,14), Moon(9,11,6), Moon(-6,14,-4), Moon(4,-4,-3)]
period = [None] * 3
visited = [set()] * 3

def findperiod(axis):
    if not period[axis]:
        pos = tuple([moon.position[axis] for moon in moons])
        vel = tuple([moon.velocity[axis] for moon in moons])
        storeme = tuple([pos, vel])
        if storeme in visited[axis]:
            period[axis] = t
        visited[axis].add(storeme)

t = 0
while(True):
    for i in range(3): findperiod(i)

    if all(period):
        print("Part 2:", reduce(lambda acc,val: acc*val // gcd(acc, val), period))
        break

    for moon1 in moons:
        for moon2 in moons:
            if not moon1 is moon2: 
                moon1.updateVelocity(moon2)

    for moon in moons:
        moon.updatePosition()
    t += 1