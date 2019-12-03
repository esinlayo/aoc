f=open("aoc3.txt", "r")


path1 = f.readline().strip("\n").split(",")
path1 = [(instr[0], int(instr[1:])) for instr in path1]
path2 = f.readline().strip("\n").split(",")
path2 = [(instr[0], int(instr[1:])) for instr in path2]
print(path1[-1], path2[-1])

#print(path1, path2)

visited1 = dict()

x1, y1 = 0,0
total_steps = 0
for dir,dist in path1:
    if dir == 'L': 
        for i in range(1,dist+1): 
            total_steps += 1
            if (x1-i, y1) not in visited1: visited1[(x1-i, y1)] = total_steps
        x1 = x1-dist
    elif dir == 'R':
        for i in range(1,dist+1): 
            total_steps += 1
            if (x1+i, y1) not in visited1: visited1[(x1+i, y1)] = total_steps
        x1 = x1+dist
    elif dir == 'U':
        for i in range(1,dist+1):
            total_steps += 1
            if (x1, y1-i) not in visited1: visited1[(x1, y1-i)] = total_steps
        y1 = y1-dist
    elif dir == 'D':
        for i in range(1,dist+1): 
            total_steps += 1
            if (x1, y1+i) not in visited1: visited1[(x1, y1+i)] = total_steps
        y1 = y1+dist

#print(visited1)

min_steps = float("inf")

x2, y2 = 0,0
total_steps = 0
for dir,dist in path2:
    if dir == 'L': 
        for i in range(1,dist+1): 
            total_steps += 1
            if (x2-i, y2) in visited1: 
                min_steps = min(min_steps, total_steps + visited1[(x2-i, y2)])
        x2 = x2-dist
    elif dir == 'R':
        for i in range(1,dist+1): 
            total_steps += 1
            if (x2+i, y2) in visited1: 
                min_steps = min(min_steps, total_steps + visited1[(x2+i, y2)])
        x2 = x2+dist
    elif dir == 'U':
        for i in range(1,dist+1): 
            total_steps += 1
            if (x2, y2-i) in visited1: 
                min_steps = min(min_steps, total_steps + visited1[(x2, y2-i)])
        y2 = y2-dist
    elif dir == 'D':
        for i in range(1,dist+1): 
            total_steps += 1
            if (x2, y2+i) in visited1: 
                min_steps = min(min_steps, total_steps + visited1[(x2, y2+i)])
        y2 = y2+dist

print(min_steps)