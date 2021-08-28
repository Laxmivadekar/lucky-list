a=[23,14,56,12,19,9,15,25,31,42,43]
i=0
e=0
o=0
c_e=0
c_o=0
while i<len(a):
    if a[i]%2==0:
        c_e=c_e+a[i]
        e=e+1
    else:
        c_o=c_o+a[i]
        o=o+1
    i=i+1
print(c_e//e)
print(c_o//o)