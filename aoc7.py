from program7 import amplifier, Amplifier

f=open("aoc7.txt", "r")

program = f.readline()

program = program.strip("\n").split(",")
program = [int(num) for num in program]

seqs = []
def generate_sequences(have = set(), sequence = []):
    if len(have) == 5:
        seqs.append(sequence[:])
        return
    for i in range(5):
        if i not in have:
            have.add(i)
            sequence.append(i)
            generate_sequences(have, sequence)
            sequence.pop()
            have.remove(i)

generate_sequences()


max_output = 0
max_seq = None
print(program, 'p')
print()
for seq in seqs:
    p1, p2, p3, p4, p5 =  seq
    A = amplifier(program, [0, p1], 'A')
    B = amplifier(program, [A, p2], 'B')
    C = amplifier(program, [B, p3], 'C')
    D = amplifier(program, [C, p4], 'D')
    E = amplifier(program, [D, p5], 'E')
    max_output = max(max_output, E)
print(max_output, max_seq)




max_output = 0
seqs = []
def generate_sequences2(have = set(), sequence = []):
    if len(have) == 5:
        seqs.append(sequence[:])
        return
    for i in range(5,10):
        if i not in have:
            have.add(i)
            sequence.append(i)
            generate_sequences2(have, sequence)
            sequence.pop()
            have.remove(i)
generate_sequences2()


for seq in seqs:
    print(seq)
    p1, p2, p3, p4, p5 =  seq
    
    A = Amplifier(program, p1, 'A')
    B = Amplifier(program, p2, 'B')
    C = Amplifier(program, p3, 'C')
    D = Amplifier(program, p4, 'D')
    E = Amplifier(program, p5, 'E')
    
    res = 0
    while True:
        res = A.run(res)
        #print(seq, 'donea', res)
        res = B.run(res)
        #print(seq, 'doneb', res)
        res = C.run(res)
        res = D.run(res)
        res = E.run(res)

        max_output = max(max_output, res)
        if E.halted: 
            print('GAHHHHHHHH'*5)
            break
print(max_output)
        
    
