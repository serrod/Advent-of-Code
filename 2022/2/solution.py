scores = {'A':1,'B':2,'C':3,'X':1,'Y':2,'Z':3}
mscore = 0
f = open("example","r")
l = f.read().split('\n')
l.pop()
print(l)

for i in range(len(l)):
    print(scores[l[i][0]])
    if scores[l[i][0]] == scores[l[i][2]]:
        mscore += scores[l[i][2]]
    elif scores[]
        print("test")
