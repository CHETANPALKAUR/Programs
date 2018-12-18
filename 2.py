import sys
s1=sys.argv[1]
s2=sys.argv[2]
e=s1[:]
for i in range(len(s2)):
    if s2[i] in s1:
        t=0
        for j in s1:
            if s2[i]==j:
                t=t+1
        for y in range(t):
            e.remove(s2[i])
e=''.join(e)
print(e)