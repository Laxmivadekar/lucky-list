n=[5,3,8,6,7,2]
i=0
while i<len(n):
    j=0
    while j<len(n)-1:
        if n[j]>n[j+1]:
            temp=n[j]
            n[j]=n[j+1]
            n[j+1]=temp
        j=j+1
    i=i+1
print(n)