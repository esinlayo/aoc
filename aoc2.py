f=open("aoc2.txt", "r")

line = f.readline()
print(line)

NOUN = 82#12
VERB = 98# 2

line = line.split(",")
line = [int(num) for num in line]
print(line[0])
line[1] = NOUN
line[2] = VERB

i = 0
while (i<len(line)):
    op_code = line[i]
    
    if op_code == 1:
        pos_1, pos_2, replace_pos = line[i+1:i+1+3]
        line[replace_pos] = line[pos_1] + line[pos_2]
    elif op_code == 2:
        pos_1, pos_2, replace_pos = line[i+1:i+1+3]
        line[replace_pos] = line[pos_1] * line[pos_2]
    elif op_code == 99:
        break
    i+=4

print(line)
print(line[0])