a=[3,4,6,2,0,0,0,0,0,0,6,7,6,9,10,0,0,0,0,7,4,4,0,0,5,3,2,9,7,1]
i=0
while i<len(a):
    b=[]
    sum=0
    j=0
    while j<=6:
        if a[i]==0:
            break
        else:
            sum=sum+a[i]
        j=j+1
    b.append(sum)
    i=i+1
print(b)