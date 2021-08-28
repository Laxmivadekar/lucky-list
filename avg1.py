a = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78]
] 
i=0
avg=0
while i<len(a):
    sum=0
    j=0
    while j<len(a):
        sum=sum+a[i][j]
        j=j+1
        avg=avg+1
    i=i+1
    print(sum//avg)
    
