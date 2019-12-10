from program7 import Amplifier

f=open("aoc5.txt", "r")

program = f.readline()

program = program.strip("\n").split(",")
program = [int(num) for num in program]

A = Amplifier(program, 1, 'aoc5')
res = A.amplify(1)
print('res',res)