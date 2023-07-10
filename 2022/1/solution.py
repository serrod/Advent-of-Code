import heapq
buffer = 0
all = []
f = open("input","r")

for line in f:
    if line != '\n':
        buffer += int(line)
    else:
        all.append(buffer)
        buffer = 0

all.append(buffer)
three = heapq.nlargest(3,all)
print(sum(three))
