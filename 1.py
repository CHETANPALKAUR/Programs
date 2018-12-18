import sys
a=sys.argv[1]
b=sys.argv[2]
t=[]
a=[int(i) for i in a]
b=[int(i) for i in b]
for i in a:
    for j in b:
        if abs(i-j)==1:
           t.append((i,j))
y=[]
for i in t:
    if i[0]>i[1]:
        y.append((i[1],i[0]))
    else:
        y.append((i[0], i[1]))
p=y[:]
l=len(y)
for i in range(l):
    b=0
    for j in range(i+1,l):
        if y[i]==y[j]:
            b=b+1

    for h in range(b):
        p.remove(y[i])
print(p)
