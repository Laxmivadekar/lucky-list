a=[[7,2,3,4,5,6],[1,2,3,4,5,6]]
i=0
b=[]
while i<=0:
    j=0
    while j<len(a[i])-1:
        j=j+1
    i=i+1
    b.append([i][j]-a[i+1][j])
print(b)
#(0r)
