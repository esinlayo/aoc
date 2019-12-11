f=open("aoc5.txt", "r")

mem = f.readline()
mem = mem.strip("\n").split(",")
mem = [int(num) for num in mem]
mem.extend([0 for _ in range(len(mem)*2)])

relative_base = 0

def getOperandValue(parameter, mode):
    if mode == 0: return mem[parameter]
    if mode == 1: return parameter
    if mode == 2: return mem[parameter + relative_base]

def getAddress(parameter, mode):
    if mode == 0: return parameter
    if mode == 1: print("this shouldnt happen")
    if mode == 2: return parameter+relative_base

i = 0
while (i<len(mem)):
    op_code = mem[i]%100                       # parameter modes: 0 memory loc, 1 immediate, 2 memory loc + relative base
    p1_mode = (mem[i] // 100) % 10
    p2_mode = (mem[i] // 1000) % 10
    p3_mode = (mem[i] // 10000) % 10
    
    param1, param2, param3 = (None if i+1 >= len(mem) else mem[i+1]), (None if i+2 >= len(mem) else mem[i+2]), (None if i+3 >= len(mem) else mem[i+3])

    if op_code == 1:
        addend1, addend2 = getOperandValue(param1, p1_mode), getOperandValue(param2, p2_mode)
        mem[getAddress(param3, p3_mode)] = addend1 + addend2
        i+=4
    elif op_code == 2:
        mul1, mul2 = getOperandValue(param1, p1_mode), getOperandValue(param2, p2_mode)
        mem[getAddress(param3, p3_mode)] = mul1 * mul2
        i+=4
    elif op_code == 3:
        val = input()
        mem[getAddress(param1, p1_mode)] = int(val)
        i+=2
    elif op_code == 4:
        print("outputting", getOperandValue(param1, p1_mode))
        i+=2
    elif op_code == 5:
        param1, param2 =  getOperandValue(param1, p1_mode), getOperandValue(param2, p2_mode)
        if param1 != 0: i = param2
        else: i+= 3
    elif op_code == 6:
        param1, param2 =  getOperandValue(param1, p1_mode), getOperandValue(param2, p2_mode)
        if param1 == 0: i = param2
        else: i+= 3
    elif op_code == 7:
        param1, param2 = getOperandValue(param1, p1_mode), getOperandValue(param2, p2_mode)
        mem[getAddress(param3, p3_mode)] = 1 if param1 < param2 else 0
        i+= 4
    elif op_code == 8:
        param1, param2 = getOperandValue(param1, p1_mode), getOperandValue(param2, p2_mode)
        mem[getAddress(param3, p3_mode)] = 1 if param1 == param2 else 0
        i+= 4
    elif op_code == 9:
        param1 = getOperandValue(param1, p1_mode)
        relative_base += param1
        i+=2
    elif op_code == 99:
        break
    else:
        print("invalid opcode", op_code)
        break