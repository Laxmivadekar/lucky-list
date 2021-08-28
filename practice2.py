a=[3,4,6,2,0,0,0,0,0,0,6,7,6,9,10,0,0,0,0,7,4,4,0,0,5,3,2,9,7,1,0,0,0,]
i=0
b=[]
while i<len(a):
    j=1
    sum=0
    while j<=8:
        sum=sum+a[i]
        j=j+1
    b.append(sum)
    i=i+8
    print(b)
