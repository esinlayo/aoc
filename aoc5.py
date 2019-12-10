f=open("aoc5.txt", "r")

line = f.readline()
#print(line)

line = line.strip("\n").split(",")
line = [int(num) for num in line]
#line += [0 for _ in range(500)]
#print(line)
#line[1] = 1

#line = [3,1] + line

waitingForInput=[]
i = 0
print(len(line), line)
while (i<len(line)):
    op_code = line[i]%100
    one_param_mode = (line[i] // 100) % 10
    two_param_mode = (line[i] // 1000) % 10
    thr_param_mode = (line[i] // 10000) % 10
    print("----", i, line[i], op_code, one_param_mode, two_param_mode, thr_param_mode)
    if thr_param_mode != 0: print("WARANING")

    try:
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
            #print('rp',replace_pos, mul1, mul2)
            line[replace_pos] = mul1 * mul2
            i+=4
        elif op_code == 3:
            pos = line[i+1]
            val = input()
            line[pos] = int(val)
            print(line[pos])
            i+=2
        elif op_code == 4:
            val = line[i+1]
            print('OUTPUT', line[val])
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
            print('weird op_code', op_code)
            i+=1
            break
    except:
        print(line)
        break

print(line)
print(line[1])