import copy

f = open("aoc24.txt", "r")

data = [list(line.strip("\n")) for line in f.readlines()]

#tuple(zip((data)))

seen = set()

while True:
    print("-------")
    for row in data:
        print(row)

    comp = tuple(s for row in data for s in row)
    if comp in seen:
        total = 0
        for i,c in enumerate(comp):
            if c == '#':
                total += 2**i
        print(total)
        break
    seen.add(comp)
    
    newdata = copy.deepcopy(data)
    for r,row in enumerate(data):
        for c,col in enumerate(row):
            cnt_bugs_adjacent = 0
            if 0 <= r+1 < len(data) and data[r+1][c] == '#': cnt_bugs_adjacent+= 1
            if 0 <= r-1 < len(data) and data[r-1][c] == '#': cnt_bugs_adjacent+= 1
            if 0 <= c+1 < len(row) and data[r][c+1] == '#': cnt_bugs_adjacent+= 1
            if 0 <= c-1 < len(row) and data[r][c-1] == '#': cnt_bugs_adjacent+= 1
            if data[r][c] == '#':
                newdata[r][c] = '#' if cnt_bugs_adjacent == 1 else '.'
            if data[r][c] == '.':
                newdata[r][c] = '#' if 1 <= cnt_bugs_adjacent <= 2 else '.'
            
    data = newdata