n=int(input('enter a number'))
i=1
a=[]
while i<=n:
    j=1
    b=[]
    while j<=10:
        b.append(i*j)
        j=j+1
    i=i+1
    a.append(b)
print(a)
