a=[1,2,3,[4,[5,6]],8,[9]]
i=0
newlist=[]
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            if type(a[i][j])==list:
                k=0
                while k<len(a[i][j]):
                    newlist.append(a[i][j][k])
                    k=k+1
            else:
                newlist.append(a[i][j])
            j=j+1
    else:
        newlist.append(a[i])
    i=i+1
    print(newlist)        