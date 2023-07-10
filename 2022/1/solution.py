buffer = 0
maxes = [0,0,0]
f = open("input","r")

for line in f:
    if line != '\n':
        buffer += int(line)
    else:
        if buffer > maxes[0]:
            maxes[2] = maxes[1]
            maxes[1] = maxes[0] 
            maxes[0] = buffer
        elif buffer > maxes[1]:
            maxes[2] = maxes[1]
            maxes[1] = buffer
        elif buffer > maxes[2]:
            maxes[2] = buffer
        buffer = 0

print(sum(maxes))
