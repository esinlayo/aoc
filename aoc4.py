startval = 359282
endval = 820401

start = [3,5,9,2,8,2]
end = [8,2,0,4,0,1]

def buildNumber(arr):
    num = 0
    for p,val in enumerate(reversed(arr)):
        num += (10**p)*val
    return num

def go():
    count = 0
    def helper(i, pw=[]):
        nonlocal count
        if i >= 6:
            if not (startval <= buildNumber(pw) <= endval): return
            if pw[0] == pw[1] or pw[1] == pw[2] or pw[2] == pw[3] or pw[3] == pw[4] or pw[4] == pw[5]: 
                print("yay", pw)
                count += 1
            else:
                print("naw", pw)
            return
        
        if i == 0:
            for j in range(3, 8+1):
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