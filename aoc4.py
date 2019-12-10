startval = 359282
endval = 820401

start = [3,5,9,2,8,2]
end = [8,2,0,4,0,1]

## Note: ya it's ugly, I just wanted it done fast

def buildNumber(arr):
    num = 0
    for p,val in enumerate(reversed(arr)):
        num += (10**p)*val
    return num

def go():

    count = 0
    def helper(i, pw=[]):
        def yaAllowed(i, j):
            return pw[i] == pw[j] and not ((i-1 >= 0 and pw[i-1] == pw[i]) or (j+1 < 6 and pw[j] == pw[j+1]))
        nonlocal count
        if i >= 6:
            if not (startval <= buildNumber(pw) <= endval): return
            if yaAllowed(0, 1) or yaAllowed(1,2) or yaAllowed(2,3) or yaAllowed(3,4) or yaAllowed(4,5):
                print("yay", pw)
                count += 1
            else:
                print("naw", pw)
            return
        
        if i == 0:
            for j in range(3, 10):
                pw.append(j)
                helper(1, pw)
                pw.pop()
        else:
            for j in range(pw[-1], 10):
                pw.append(j)
                helper(i+1, pw)
                pw.pop()
            
    helper(0)
    print(count)

go()