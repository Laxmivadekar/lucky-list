a=[23,14,56,12,19,9,15,25,31,42,43]
i=0
b=[]
c=[]
while i<len(a):
    if a[i]%2==0:
        b.append (a[i])
    else:
        c.append (a[i])
    i=i+1
print('even no.',b)
print('odd no',c)