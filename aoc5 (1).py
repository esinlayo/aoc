f=open("aoc5.txt", "r")

line = f.readline()
line = line.strip("\n").split(",")
line = [int(num) for num in line]

i = 0
while (i<len(line)):
    op_code = line[i]%100                       # parameter modes: 0 memory loc, 1 immediate, 2 memory loc + relative base
    one_param_mode = (line[i] // 100) % 10
    two_param_mode = (line[i] // 1000) % 10
    thr_param_mode = (line[i] // 10000) % 10
    
    if op_code == 1:
        addend1 = line[i+1] if one_param_mode else line[line[i+1]]
        addend2 = line[i+2] if two_param_mode else line[line[i+2]]
        replace_pos = line[i+3] if not thr_param_mode else line[line[i+3]]
        line[replace_pos] = addend1 + addend2
        i+=4
    elif op_code == 2:
        mul1 = line[i+1] if one_param_mode else line[line[i+1]]
        mul2 = line[i+2] if two_param_mode else line[line[i+2]]
        replace_pos = line[i+3] if not thr_param_mode else line[line[i+3]]
        line[replace_pos] = mul1 * mul2
        i+=4
    elif op_code == 3:
        if one_param_mode or two_param_mode or thr_param_mode: print("WARNING, WEIRD MODE WITH OPCODE 3")
        pos = line[i+1]
        val = input()
        line[pos] = int(val)
        print(line[pos])
        i+=2
    elif op_code == 4:
        val = line[i+1]
        output = val if one_param_mode else line[val]
        print(output)
        i+=2
    elif op_code == 5:
        param1, param2 = line[i+1:i+3]
        param1 = param1 if one_param_mode else line[param1]
        param2 = param2 if two_param_mode else line[param2]
        if param1 != 0: 
            i = param2
            continue
        i+= 3
    elif op_code == 6:
        param1, param2 = line[i+1:i+3]
        param1 = param1 if one_param_mode else line[param1]
        param2 = param2 if two_param_mode else line[param2]
        if param1 == 0: 
            i = param2
            continue
        i+= 3
    elif op_code == 7:
        param1, param2, param3 = line[i+1:i+4]
        param1 = param1 if one_param_mode else line[param1]
        param2 = param2 if two_param_mode else line[param2]
        param3 = param3 if not thr_param_mode else line[param3]
        line[param3] = 1 if param1 < param2 else 0
        i+= 4
    elif op_code == 8:
        param1, param2, param3 = line[i+1:i+4]
        param1 = param1 if one_param_mode else line[param1]
        param2 = param2 if two_param_mode else line[param2]
        param3 = param3 if not thr_param_mode else line[param3]
        line[param3] = 1 if param1 == param2 else 0
        i+= 4
    elif op_code == 99:
        break
    else:
        print("invalid opcode")