import os
import time


f = open("aoc16.txt", "r")
line = f.readline()
offset = line[:7]


signal = [int(dig) for dig in line.strip("\n")]

signal = signal*10000
offset = int(offset)
print("signal length", len(signal))
print("offset length", offset)
signal = signal[offset:]
start_time = time.time()
signal2 = [0 for _ in range(len(signal))]
for i in range(100):
    print("fft run", i, end='  ')
    '''
    for j in range(len(signal2)):
        signal2[j] = abs(sum(signal[j:])) % 10
    print(signal2[:8], ' ', end='')
    #'''
    runningsignal = sum(signal)
    for j in range(len(signal)):
        signal2[j] = abs(runningsignal) % 10
        runningsignal -= signal[j]
    print(signal2[:8])
    signal = signal2[:]
print("--- %s seconds ---" % (time.time() - start_time))
print(signal[:8])
