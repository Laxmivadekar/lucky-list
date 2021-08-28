i=1
a=[]
while i<=10:
    n=int(input('enter a number'))
    a.append(n)
    i=i+1
print(a)
j=0
while j<len(a):
    b=int(input('enter a number'))
    if b in a:
        print(b,'is in a')
    else:
        print(b,'1 is not in a')
    j=j+1


