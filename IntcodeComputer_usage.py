from IntcodeComputer import IntcodeComputer

def createMem(str):
    str = str.strip("\n").split(",")
    str = [int(num) for num in str]
    str.extend([0 for _ in range(len(str)*len(str))])
    return str

def simpleTest(machine, input, expectedO):
    machine.run([input])
    while not machine.halted:
        machine.run()
    assert machine.output[-1] == expectedO, (input, machine.output)

def entireOutputTest(machine, input, expectedO):
    machine.run([input])
    while not machine.halted:
        machine.run()
    assert machine.output == expectedO, (machine.output, expectedO)



######## DAY 5 TESTS
test1, test2, test3, test4 = "3,9,8,9,10,9,4,9,99,-1,8", "3,9,7,9,10,9,4,9,99,-1,8", "3,3,1108,-1,8,3,4,3,99", "3,3,1107,-1,8,3,4,3,99"
test5, test6 = "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9", "3,3,1105,-1,9,1101,0,0,12,4,12,99,1"

# Test 1
simpleTest(IntcodeComputer(createMem(test1)), 8, 1)
simpleTest(IntcodeComputer(createMem(test1)), -4, 0)
simpleTest(IntcodeComputer(createMem(test1)), 10, 0)
# Test 2
simpleTest(IntcodeComputer(createMem(test2)), 8, 0)
simpleTest(IntcodeComputer(createMem(test2)), -4, 1)
simpleTest(IntcodeComputer(createMem(test2)), 10, 0)
# Test 3
simpleTest(IntcodeComputer(createMem(test3)), 8, 1)
simpleTest(IntcodeComputer(createMem(test3)), -4, 0)
simpleTest(IntcodeComputer(createMem(test3)), 10, 0)
# Test 4
simpleTest(IntcodeComputer(createMem(test4)), 7, 1)
simpleTest(IntcodeComputer(createMem(test4)), -4, 1)
simpleTest(IntcodeComputer(createMem(test4)), 8, 0)
simpleTest(IntcodeComputer(createMem(test4)), 10, 0)
# Test 5
simpleTest(IntcodeComputer(createMem(test5)), 0, 0)
simpleTest(IntcodeComputer(createMem(test5)), -4, 1)
simpleTest(IntcodeComputer(createMem(test5)), 10, 1)
# Test 6
simpleTest(IntcodeComputer(createMem(test6)), 0, 0)
simpleTest(IntcodeComputer(createMem(test6)), -4, 1)
simpleTest(IntcodeComputer(createMem(test6)), 10, 1)

######## DAY 5
aoc5 = createMem(open("aoc5.txt").readline())

# Part 1
amply = IntcodeComputer(aoc5)
amply.run([2])
while not amply.halted:
    amply.run()
print("Day 5 Part 1:", amply.output)

# Part 2
amply = IntcodeComputer(aoc5)
amply.run([5])
while not amply.halted:
    amply.run()
print("Day 5 Part 2:", amply.output)







######## DAY 7
Amplifier = IntcodeComputer
aoc7 = createMem(open("aoc7.txt", "r").readline())
mem = aoc7

def generate_sequences(iter, have = set(), sequence = [], allSeqs = []):
    if len(have) == 5:
        allSeqs.append(sequence[:])
        return
    for i in iter:
        if i not in have:
            have.add(i)
            sequence.append(i)
            generate_sequences(iter, have, sequence)
            sequence.pop()
            have.remove(i)
    return allSeqs

max_output = 0
for seq in generate_sequences(range(5)):
    p1, p2, p3, p4, p5 =  seq
    A = Amplifier(mem, p1)
    B = Amplifier(mem, p2)
    C = Amplifier(mem, p3)
    D = Amplifier(mem, p4)
    E = Amplifier(mem, p5)
    a = A.run([0])
    b = B.run([a])
    c = C.run([b])
    d = D.run([c])
    e = E.run([d])
    max_output = max(max_output, E.output[-1])
print("Day 7 Part 1:", max_output)

max_output = 0
for seq in generate_sequences(range(5,10)):
    p1, p2, p3, p4, p5 =  seq
    A = Amplifier(mem, p1)
    B = Amplifier(mem, p2)
    C = Amplifier(mem, p3)
    D = Amplifier(mem, p4)
    E = Amplifier(mem, p5)
    
    res = 0
    while True:
        res = A.run([res])
        res = B.run([res])
        res = C.run([res])
        res = D.run([res])
        res = E.run([res])
        if E.halted: break
    max_output = max(max_output, E.output[-1])
print("Day 7 Part 2:", max_output)






######## DAY 9 TESTS
test1, test2, test3 = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99", "1102,34915192,34915192,7,4,7,99,0", "104,1125899906842624,99"

# Test 1
entireOutputTest(IntcodeComputer(createMem(test1)), None, [int(num) for num in test1.split(",")])
# Test 2
#simpleTest(IntcodeComputer(createMem(test2)), None, 0) #length is 16
# Test 3
simpleTest(IntcodeComputer(createMem(test3)), None, 1125899906842624)

######## DAY 9
aoc9 = createMem(open("aoc9.txt", "r").readline())

# Part 1
machine = IntcodeComputer(aoc9)
machine.run([1])
while not machine.halted:
    machine.run()
print("Day 9 Part 1:", machine.output)

# Part 2
machine = IntcodeComputer(aoc9)
machine.run([2])
while not machine.halted:
    machine.run()
print("Day 9 Part 2:", machine.output)