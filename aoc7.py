from IntcodeComputer import IntcodeComputer as Amplifier

f=open("aoc7.txt", "r")

mem = f.readline()
mem = mem.strip("\n").split(",")
mem = [int(num) for num in mem]
mem.extend([0 for _ in range(len(mem)*len(mem))])

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
print("Part1", max_output)


print("--------------------------------------------------------------------------")


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
print("Part2", max_output)

