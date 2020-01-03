from collections import deque
import math

f = open("aoc22.txt")
data = [line.strip("\n") for line in f.readlines()]

'''
deck = [i for i in range(10007)]

print(deck)
for move in data:
    print(move)
    if move[:4] == "cut ":
        amt = int(move[4:])
        deck = deck[amt:] + deck[:amt]
    elif move[:9] == "deal into":
        deck = list(reversed(deck))
    elif move[:20] == "deal with increment ":
        inc = int(move[20:])
        newdeck = ["_" for i in range(len(deck))]
        lend = len(newdeck)
        i = 0
        while(i < lend):
            newdeck[(inc*i) % lend] = deck.pop(0)
            i += 1
        deck = newdeck

print(deck)
print(deck.index(2019))
'''

deck = [i for i in range(119315717514047)]
j = 0
while(j < 119315717514047):
    j += 1
    if j % 100000:
        print(j)
    for move in data:
        if move[:4] == "cut ":
            amt = int(move[4:])
            deck = deck[amt:] + deck[:amt]
        elif move[:9] == "deal into":
            deck = list(reversed(deck))
        elif move[:20] == "deal with increment ":
            inc = int(move[20:])
            newdeck = ["_" for i in range(len(deck))]
            lend = len(newdeck)
            i = 0
            while(i < lend):
                newdeck[(inc*i) % lend] = deck.pop(0)
                i += 1
            deck = newdeck

print(deck.index(2020))
