import os

f = open("aoc16.txt", "r")
signal = f.readline().strip("\n")

signal = list(map(int,signal))
signal = signal


def getStuff(n, length):
    n = n+1
    base = [0]*n + [1]*n + [0]*n + [-1]*n
    while (len(base) < length+1):
        base.extend(base)
    return base[1:length+1]

muls = []
for i in range(len(signal)):
    muls.append(getStuff(i, len(signal)))

for mul in muls:
    #print(mul)
    pass
print()


def runPhase(signal):
    newsignal = []
    for i in range(len(signal)):
        val = 0
        for elem,mul in zip(signal, muls[i]):
            val += elem*mul
        newsignal.append(abs(val)%10)
    return newsignal

i_signal = signal[:]

for i in range(100):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(i)
    signal = runPhase(signal)
    #print(signal)

print(i_signal)
print(signal)


print(len(signal), len(signal)*10000, ''.join(str(i) for i in i_signal[:7]))