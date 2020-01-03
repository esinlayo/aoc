from collections import deque
import os
import sys
os.system('cls' if os.name == 'nt' else 'clear')
sys.setrecursionlimit(10000)

f = open("aoc18.txt", "r")
matrix = [list(row.strip("\n")) for row in f.readlines()]
lmt_row, lmt_col = len(matrix), len(matrix[0])

startPos = (None,None)
keys_cnt = 0

for r,row in enumerate(matrix):
    for c,col in enumerate(row):
        if matrix[r][c] == '@': 
            startPos = (r,c)
            matrix[r][c] = '.'
        if matrix[r][c].islower(): keys_cnt += 1

print("Number of keys:", keys_cnt)

for i in range(len(matrix[0])): print(i, end='')
print()
for row in matrix:
    for e in row:
        print(e, end='')
    print()

def bfs():
    visited = set((startPos, frozenset()))            # r, c, keys I have

    Q = deque([(startPos, set())])
    Q_length = 1
    shortest_path_length = 0

    while Q:
        #print(Q)
        #input()
        shortest_path_length += 1
        num_adjacent = 0
        popped= 0
        while Q and popped < Q_length:
            popped += 1
            (currR, currC), currKeys = Q.popleft()
            
            for incr,incc in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                nextR, nextC = currR + incr, currC + incc
                if 0 <= nextR < lmt_row and 0 <= nextC < lmt_col:
                    nextKeys = set(currKeys)
                    if matrix[nextR][nextC].islower(): nextKeys.add(matrix[nextR][nextC])
                    
                    next_coord = (nextR, nextC)
                    if (next_coord, frozenset(currKeys)) not in visited \
                            and (matrix[nextR][nextC] == '.' \
                                    or matrix[nextR][nextC].islower() \
                                    or (matrix[nextR][nextC].isupper() and matrix[nextR][nextC].lower() in currKeys)):

                        
                        if len(nextKeys) == keys_cnt:
                            Q.clear()
                            print('HELLLO')
                            print(shortest_path_length)
                            return
                        
                        item = (next_coord, frozenset(nextKeys))
                        visited.add(item)
                        Q.append(item)
                        num_adjacent += 1

        Q_length = num_adjacent
        
bfs()