a=[[78,76,94,86,88],[91,71,98,65,76],[95,45,78,52,49]]
i=0
while i<len(a):
    sum=0
    j=1
    while j<len(a[i]):
        sum=a[i][j]+sum
        j=j+1
    i=i+1
print(sum//5)
