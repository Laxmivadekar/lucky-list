a= [1,2,3,2,1,3,12,12,32]
i=0
b=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i=i+1
print(b)

















#OUTPUT : [1,2,3,12,32]