def go(mass):
    return mass//3-2

res1 = 0
res2 = 0

f=open("nums.txt", "r")

f1 = f.readlines()
for num in f1:
    res1 += int(num)//3-2
    
    temp = int(num)
    
    while(temp > 0):
        fuel = temp//3 - 2
        if (fuel > 0):
            res2 += fuel
        temp = fuel
print(res2)

