f=open("aoc8.txt", "r")
data = f.readline().strip("\n")

width = 25
height = 6

layers = []

i = 0
while(i<len(data)):
    layer = []
    m = 0
    while(m < width*height):
        row = data[i+m:i+m+width]
        row = [int(val) for val in row]
        layer.append(row)
        m += width
        
    i += width*height
    layers.append(layer)

fewers_zeros = float("inf")
layer_number = 0
    
for l,layer in enumerate(layers):
    cnt_zeros = sum((1 if val == 0 else 0 for row in layer for val in row))
    if cnt_zeros < fewers_zeros: fewers_zeros, layer_number = cnt_zeros, l

num_1s = sum((1 if val == 1 else 0 for row in layers[layer_number] for val in row))
num_2s = sum((1 if val == 2 else 0 for row in layers[layer_number] for val in row))
print(num_1s*num_2s)







image = [[2 for _ in range(width)] for _ in range(height)]

for layer in layers:
    for r,row in enumerate(layer):
        for c,val in enumerate(row):
            if image[r][c] == 2:
                image[r][c] = val

for row in image:
    print(row)