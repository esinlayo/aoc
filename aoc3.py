f=open("aoc3_smol.txt", "r")


path1 = f.readline().strip("\n").split(",")
path1 = [(instr[0], int(instr[1:])) for instr in path1]
path2 = f.readline().strip("\n").split(",")
path2 = [(instr[0], int(instr[1:])) for instr in path2]
print(path1[-1], path2[-1])

#print(path1, path2)

visited1 = set()

x1, y1 = 0,0
for dir,dist in path1:
    if dir == 'L': 
        for i in range(1,dist+1): visited1.add((x1-i, y1))
        x1 = x1-dist
    elif dir == 'R':
        for i in range(1,dist+1): visited1.add((x1+i, y1))
        x1 = x1+dist
    elif dir == 'U':
        for i in range(1,dist+1): visited1.add((x1, y1-i))
        y1 = y1-dist
    elif dir == 'D':
        for i in range(1,dist+1): visited1.add((x1, y1+i))
        y1 = y1+dist

#print(visited1)

crosspoints = []
x2, y2 = 0,0
for dir,dist in path2:
    if dir == 'L': 
        for i in range(1,dist+1): 
            if (x2-i, y2) in visited1: 
                crosspoints.append((x2-i, y2))
        x2 = x2-dist
    elif dir == 'R':
        for i in range(1,dist+1): 
            if (x2+i, y2) in visited1: 
                crosspoints.append((x2+i, y2))
        x2 = x2+dist
    elif dir == 'U':
        for i in range(1,dist+1): 
            if (x2, y2-i) in visited1: 
                crosspoints.append((x2, y2-i))
        y2 = y2-dist
    elif dir == 'D':
        for i in range(1,dist+1): 
            if (x2, y2+i) in visited1: 
                crosspoints.append((x2, y2+i))
        y2 = y2+dist

print(crosspoints)
crosspoints = [sum([abs(val) for val in cx]) for cx in crosspoints]
print(crosspoints)
print(min(crosspoints))