import sys

u=sys.argv[1]
t=u.split()
day=int(t[0])
month=t[1]
year=int(t[2])
m=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
m1=['Jan','Mar','May','Jul','Aug','Oct','Dec']
if day<28:
    day=day+1
else:
    y=year/4
    y1=year//4
    t=1
    if y==y1:
        t=0
    if month=='Feb' and t:
        day='1'
        month='Mar'
    elif month=='Feb':
        day=day+1
    elif day<31:
        day=day+1
    else:
        if month in m1 and (day!=31):
            day=day+1
        else:
            day='1'
            for j in range(len(m)):
                if month==m[j]:
                    p=j
                    break
            if j==11:
                month=m[0]
                year=year+1
            else:
                month=m[j+1]
print('{} {} {}'.format(day, month, year))