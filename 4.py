import sys
a=sys.argv[1]
r=len(a)
c=len(a[0])

j=0
n=0
while j<r and n<c:
    for i in range(n,c):
        print(a[j][i],end=' ')
    j=j+1
    for i in range(j,r):
        print(a[i][c-1],end=' ')

    c=c-1
    if  j<r:
        for i in range(c-1,n-1,-1):
            print(a[r-1][i],end=' ')
    r=r-1
    if n<c:
        for i in range(r-1,j-1,-1):
            print(a[i][n],end=' ')
    n=n+1

