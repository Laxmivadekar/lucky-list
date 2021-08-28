a=input('enter the name')
b='abcdefghijklmnopqrstuvwxyz'
c='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
i=0
c=0
d=0
while i<len(a):
    if a[i] in b:
        c=c+1
    else:
        d=d+1
    i=i+1
print('small letters',c)
print('capital letters',d) 