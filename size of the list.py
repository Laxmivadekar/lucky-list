a=[1,2,3,4,5,6,7,8,9,10]
b=[]
n=int(input('enter the size the of the list'))
i=0
while i<len(a):
    j=0
    c=[]
    while j<=len(str(n)):
        d=i+j
        c.append(a[d])
        j=j+1
    i=i+n
    b.append(c)
print(b)