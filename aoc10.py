f = open("aoc10.txt", "r")

filedata = f.read()
filedata = filedata.split("\n")
bestdata = [[] for _ in range(len(filedata))]
for r, row in enumerate(filedata):
    filedata[r] = [val for val in row]
    bestdata[r] = [0 for val in row]

maxlen = 0

for r, row in enumerate(filedata):
    for c, val in enumerate(row):
        if val == '#':
            see = set()

            for r2, row2 in enumerate(filedata):
                for c2, val2 in enumerate(row2):
                    if val2 == '#':
                        # calculate slope
                        if (c == c2 and r == r2):
                            continue

                        elif r2-r != 0 and c2-c != 0:
                            see.add(((c2-c)/(r2-r), c2-c > 0, r2-r > 0))

                        elif c2-c == 0:
                            if r2-r > 0:
                                see.add('+r')
                            if r2-r < 0:
                                see.add('-r')

                        elif r2-r == 0:
                            if c2-c > 0:
                                see.add('+c')
                            if c2-c < 0:
                                see.add('-c')
            bestdata[r][c] = see
            maxlen = max(maxlen, len(see))

for row in filedata:
    print(row)

print('---')

# for row in bestdata:
#    print(row)
print(bestdata[2][2])

print(maxlen)
