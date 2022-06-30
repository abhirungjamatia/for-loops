l=[13,12,21,16,6,7,4]
s=2
s1=3
for i in l:
    if i%4==0:
        s=s+i
        continue
    if i%7==0:
        s1=s1+i
print(s,end=' ')
print(s1)