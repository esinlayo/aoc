'''
current vies of scaffolds

sum of the alignment parameters 
    of the scaffold intersections
'''
import os
from IntcodeComputer import IntcodeComputer, createMemFromStr
from collections import defaultdict

asciii = {35: '#', 46: ".", 10: "\n"}
f = open("aoc17.txt", "r")

machine = IntcodeComputer(createMemFromStr(f.readline()))
while(not machine.halted):
    machine.run()
for i in range(100):
    print(i % 10, end='')
print()
row = 0
for i in machine.output:
    if chr(i) == '\n':
        print(row, end='')
        row += 1
    print(chr(i), end='')
for i in range(100):
    print(i % 10, end='')

''' googled
24*8
+48*14
+46*18

+48*28
+48*22

+22*42
+20*42

+40*18

+40*10
+44*8
'''

print("\n\n\n")

print("Part 2")

'''
wake robot up - machine.mem[0] = 2

input instructions provided as ASCII code:
    main movement routine, then a new line
        A,B,C       (movement functions)
    prompt for EACH movement function:
        L to turn left (rotate)
        R to turn right (rotate)
        or a number to move forward that many units
    continuous video feed?
        y or n and then a newline
    
'''

# note: 34 moves total
# 14+8+9 = 31

# 12 + 9 +9

move = "L,10,R,8,R,6,R,10,L,12,R,8,L,12,L,10,R,8,R,6,R,10,L,12,R,8,L,12,L,10,R,8,R,8,L,10,R,8,R,8,L,12,R,8,L,12,L,10,R,8,R,6,R,10,L,10,R,8,R,8,L,10,R,8,R,6,R,10"
counts = defaultdict(int)
for i in range(len(move)):
    for seq in ("L,10,R,8", "R,6,R,10", "L,12,R,8,L,12", "L,10,R,8,R,8", "L,10,R,8,R,6"):
        counts[seq] += 1 if move[i:i+len(seq)] == seq else 0

print(counts)


main = list(map(ord, "A,B,A,B,C,C,B,A,C,A\n"))
A = list(map(ord, "L,10,R,8,R,6,R,10\n"))
B = list(map(ord, "L,12,R,8,L,12\n"))
C = list(map(ord, "L,10,R,8,R,8\n"))
vid = list(map(ord, "n\n"))
total = main + A + B + C + vid
print(total)

# input =
f = open("aoc17.txt", "r")
machine = IntcodeComputer(createMemFromStr(f.readline()), total)
machine.mem[0] = 2
while(not machine.halted):
    machine.run()
print()
print("output")
print(machine.output)
