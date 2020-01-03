from collections import deque
import os
import sys
os.system('cls' if os.name == 'nt' else 'clear')
sys.setrecursionlimit(10000)

f = open("aoc20.txt", "r")
matrix = [row.strip("\n") for row in f.readlines()]


''' Get maze boundary values (I just hardcoded everything below though...) '''
n_rows = len(matrix)
outer_l, inner_l, inner_r, outer_r = 2, None, None, None
i = 2
while (i < len(matrix[n_rows//2])):
    while not inner_l:
        if matrix[n_rows//2][i] not in ('.', '#'):
            inner_l = i-1
        i += 1
    while matrix[n_rows//2][i] == ' ':
        i += 1
    if matrix[n_rows//2][i].isalnum():
        inner_r = i + 2
        i += 2
    else:
        inner_r = i
        i += 1
    while not outer_r:
        if matrix[n_rows//2][i] not in ('.', '#'):
            outer_r = i-1
        i += 1
    i+=1
#print(outer_l, inner_l, inner_r, outer_r)



''' Get outer portal data '''
outerportals_top = {}
outerportals_bottom = {}
outerportals_left = {}
outerportals_right = {}

for i, (e0, e1) in enumerate(zip(matrix[0], matrix[1])):
    if e0 != ' ':
        outerportals_top[f'{e0}{e1}'] = (2, i)
for i, (e0, e1) in enumerate(zip(matrix[109], matrix[110])):
    if e0 != ' ':
        outerportals_bottom[f'{e0}{e1}'] = (108, i)
for r, row in enumerate(matrix):
    if row[0] != ' ':
        outerportals_left[f'{row[0]}{row[1]}'] = (r, outer_l)
    if row[outer_r+1] != ' ':
        outerportals_right[f'{row[outer_r+1]}{row[outer_r+2]}'] = (r, outer_r)

outerportals = {}
outerportals.update(outerportals_top)
outerportals.update(outerportals_bottom)
outerportals.update(outerportals_left)
outerportals.update(outerportals_right)


''' Get inner and outer portal data (necessary to differentiate them for Part 2) '''
outer_portals, inner_portals = {}, {}

for c, (e0, e1) in enumerate(zip(matrix[27][27:78], matrix[28][27:78])):
    c += 27
    if e0 != ' ':
        symbol = f'{e0}{e1}'
        innerportal_coord, outerportal_coord = (26, c), outerportals[symbol]
        inner_portals[innerportal_coord] = outerportal_coord
        outer_portals[outerportal_coord] = innerportal_coord
for c, (e0, e1) in enumerate(zip(matrix[82][27:78], matrix[83][27:78])):
    c += 27
    if e0 != ' ':
        symbol = f'{e0}{e1}'
        innerportal_coord, outerportal_coord = (84, c), outerportals[symbol]
        inner_portals[innerportal_coord] = outerportal_coord
        outer_portals[outerportal_coord] = innerportal_coord
for r, row in enumerate(matrix):
    if not 27 <= r < 78:
        continue
    if row[27] != ' ':
        symbol = f'{row[27]}{row[28]}'
        innerportal_coord, outerportal_coord = (r, 26), outerportals[symbol]
        inner_portals[innerportal_coord] = outerportal_coord
        outer_portals[outerportal_coord] = innerportal_coord
    if row[76] != ' ':
        symbol = f'{row[76]}{row[77]}'
        innerportal_coord, outerportal_coord = (r, 78), outerportals[symbol]
        inner_portals[innerportal_coord] = outerportal_coord
        outer_portals[outerportal_coord] = innerportal_coord

portals = {}
portals.update(inner_portals)
portals.update(outer_portals)



''''''''' PART 1 '''''''''
mat1 = [list(row) for row in matrix]

def printmat(mat):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in mat:
        for e in row:
            print(e, end='')
        print()

starting_point = (108, 37)
ending_point = (2, 35)

mat1[starting_point[0]][starting_point[1]] = '█'
Q = deque([starting_point])
Q_length = 1
shortest_path_length = 0

while(Q):
    shortest_path_length += 1

    num_adjacent = 0
    popped = 0
    while Q and popped < Q_length:
        popped += 1
        currR, currC = Q.popleft()

        for incr, incc in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            r, c = currR + incr, currC + incc
            if (r, c) == ending_point:
                Q.clear()
                break
            if 2 <= r <= 108 and 2 <= c <= 102 and mat1[r][c] == '.':
                mat1[r][c] = '█'
                Q.append((r, c))
                num_adjacent += 1

        if (currR, currC) in portals:
            r, c = portals[(currR, currC)]
            if mat1[r][c] == '.':
                mat1[r][c] = '█'
                Q.append((r, c))
                num_adjacent += 1

    Q_length = num_adjacent
print("Part 1:", shortest_path_length)
print()







''''''''' PART 2 '''''''''

deepest_level = 0
mat_outside = [list(row) for row in matrix]
mat_inside = [list(row) for row in matrix]

for r,c in outerportals.values():
    if (r,c) not in (starting_point, ending_point):
        mat_outside[r][c] = '#'

visited = set()
starting_point = ((108, 37),0)
ending_point = ((2, 35), 0)

visited.add(starting_point)
Q = deque([starting_point])
Q_length = 1
shortest_path_length = 0

while(Q):
    shortest_path_length += 1

    num_adjacent = 0
    popped = 0
    while Q and popped < Q_length:
        popped += 1
        curr_place = Q.popleft()

        (currR, currC), currLevel = curr_place
        deepest_level = max(deepest_level, currLevel)
            
        if (currLevel == 200):
            print("too deep rip", '!' if Q.clear() else '')
            break

        for incr, incc in ((0, -1), (0, 1), (-1, 0), (1, 0)):                                   # left, right, up, down
            nextR, nextC = currR + incr, currC + incc
            next_place = ((nextR, nextC), currLevel)

            if next_place == ending_point:                                                      # Found the end of the maze!!!
                print("Hell ya", '!' if Q.clear() else '')
                break

            if 2 <= nextR <= 108 and 2 <= nextC <= 102 \
                    and next_place not in visited \
                    and ((currLevel == 0 and mat_outside[nextR][nextC] == '.')
                      or (currLevel > 0 and mat_inside[nextR][nextC] == '.')):

                visited.add(next_place)
                Q.append(next_place)
                num_adjacent += 1

        if (currR, currC) in portals:                                                           # Are we currently standing on a portal?
            if curr_place == starting_point: continue
            nextR, nextC = portals[(currR, currC)]                                              # Where will the portal take us?
            nextLevel = currLevel +(1 if (currR, currC) in inner_portals else -1)               # It will take us deeper if an inner portal, out if outer portal
            next_place = ((nextR, nextC), nextLevel)
            
            if next_place not in visited:
                visited.add(next_place)
                Q.append(next_place)
                num_adjacent += 1

    Q_length = num_adjacent

print("Part 2:", shortest_path_length)
print("Deepest we went was", deepest_level)





'''
dat_step_count_doe = 0

def dfs(r, c, level, steps, visited):
    global dat_step_count_doe
    data = ((r,c), level)
    print(data)
    visited.add(data)

    if level == 0:
        if (r, c) == ending_point:
            dat_step_count_doe = steps

        for incr, incc in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            nextR, nextC = r+incr, c+incc
            if 2 <= nextR <= 108 and 2 <= nextC <= 102 and mat_outside[nextR][nextC] == '.' and ((nextR, nextC), level) not in visited:
                dfs(nextR, nextC, level, steps+1, visited)
        if (r, c) in inner_portals:
            nextR, nextC = inner_portals[(r, c)]
            dfs(nextR, nextC, level+1, steps+1, visited)
    else:
        for incr, incc in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            nextR, nextC = r+incr, c+incc
            if 2 <= nextR <= 108 and 2 <= nextC <= 102 and mat_inside[nextR][nextC] == '.' and ((nextR, nextC), level) not in visited:
                dfs(nextR, nextC, level, steps+1, visited)
        if (r, c) in inner_portals:
            nextR, nextC = inner_portals[(r, c)]
            if ((nextR, nextC), level+1) not in visited:
                dfs(nextR, nextC, level+1, steps+1, visited)
        if (r, c) in outer_portals:
            nextR, nextC = outer_portals[(r, c)]
            if ((nextR, nextC), level-1) not in visited:
                dfs(nextR, nextC, level-1, steps+1, visited)

    visited.remove(((r,c), level))


r, c = starting_point
print("run dat dfs")
dfs(r, c, 0, 0, set())
print("Part 2:", dat_step_count_doe)
'''