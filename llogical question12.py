a=[58,24,13,15,63,9,8,81,1,78]
i=0
b=[]
c=[]
while i<len(a):
    if a[i]<a[4]:
        b.append(a[i])
    else:
        c.append(a[i])
    i=i+1
    print(b)
print(c)