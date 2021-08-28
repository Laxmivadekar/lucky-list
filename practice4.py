a=[1,2,3,4,5,6,7,8,9,10]
i=0
b=[]
while i<len(a):
    j=1
    c=[]
    while j<=10:
        c.append(a[i]*j)
        j=j+1
    i=i+1
    b.append(c)
print(b)
    
