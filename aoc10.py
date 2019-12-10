f = open("aoc10.txt", "r")

filedata = f.read()
filedata = filedata.split("\n")
bestdata = [[] for _ in range(len(filedata))]
for r, row in enumerate(filedata):
    filedata[r] = [val for val in row]
    bestdata[r] = [None for val in row]

maxlen = 0
bestAsteroid = None

for r, row in enumerate(filedata):
    for c, val in enumerate(row):
        if val == '#':
            see = set()

            for r2, row2 in enumerate(filedata):
                for c2, val2 in enumerate(row2):
                    if val2 == '#':
                        if (c == c2 and r == r2):
                            continue
                        elif r2-r != 0 and c2-c != 0:
                            # diag[1] means to the right, diag[2] means to below
                            see.add((abs((r2-r)/(c2-c)), c2-c > 0, r2-r > 0))

                        elif c2-c == 0:
                            if r2-r > 0:                                            # to the bottom
                                see.add('+r')
                            if r2-r < 0:
                                see.add('-r')

                        elif r2-r == 0:
                            if c2-c > 0:                                            # to the right
                                see.add('+c')
                            if c2-c < 0:
                                see.add('-c')
            bestdata[r][c] = see
            if len(see) > maxlen:
                bestAsteroid = (r, c)
            maxlen = max(maxlen, len(see))

print('Part1', maxlen)
print('---')
print(bestAsteroid, "note the mixed up order of r and c")


r, c = bestAsteroid
see = bestdata[r][c]
# print(see)

# diag[1] means to the right, diag[2] means to below
ordering = []
if '-r' in see:
    ordering.append("-r")
sortThisShit = []
for diag in see:
    if len(diag) > 2 and diag[1] and not diag[2]:   # top-right quadrant
        sortThisShit.append(diag)
ordering.extend([elem for elem in sorted(sortThisShit)])
print("len of ordering after quadrant 1", len(ordering))
if '+c' in see:
    ordering.append("+c")
sortThisShit.clear()
for diag in see:
    if len(diag) > 2 and diag[1] and diag[2]:   # bottom-right quadrant
        sortThisShit.append(diag)
ordering.extend(sorted(sortThisShit))
print("len of ordering after quadrant 2", len(ordering))
if '+r' in see:
    ordering.append("+r")
sortThisShit.clear()
for diag in see:
    if len(diag) > 2 and not diag[1] and diag[2]:   # bottom-left quadrant
        sortThisShit.append(diag)
ordering.extend(sorted(sortThisShit, reverse=True))
print("len of ordering after quadrant 3", len(ordering))
if '-c' in see:
    ordering.append('-c')
sortThisShit.clear()
for diag in see:
    if len(diag) > 2 and not diag[1] and not diag[2]:   # top-left quadrant
        sortThisShit.append(diag)
ordering.extend(sorted(sortThisShit))
print("len of ordering after quadrant 4", len(ordering))

# print(ordering)


hit200th = ordering[199]
print(hit200th)     # .833333334            # 5 rise, 6 run
rise, run = 5, 6
angle, totheright, tothebottom = hit200th
xinc = run if totheright else -run
yinc = rise if tothebottom else -rise

while True:
    if filedata[r+yinc][c+xinc] == '#':
        # Note final reversal cuz of shitty coordinate system used by the aliens
        print("Part2", ((c+xinc)*100 + (r+yinc)))
        break
    xinc += xinc
    yinc += yinc
