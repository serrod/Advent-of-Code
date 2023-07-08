l = []
buffer = 0
max = 0
f = open("input","r")

for line in f:
    if line != '\n':
        buffer += int(line)
    else:
        if buffer > max:
            max = buffer
        buffer = 0
print(max)

