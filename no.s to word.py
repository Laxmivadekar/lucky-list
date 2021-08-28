a=[250,251,252,253,254,255]
i=0
list1=[]
while i<len(list):
    j=0
    str=''
    while j<len(str(a[i]):
        if str(a[i][j])=='0':
            str+='zero'
        elif str(a[i][j])=='1':
            str+='one'
        elif str(a[i][j])=='2':
            str+='two'
        elif str(a[i][j])=='3':
            str+='three'
        elif str(a[i][j])=='4':
            str+='four'
        elif str(a[i][j])=='5':
            str+='five'
        elif str(a[i][j])=='6':
            str+='six'
        elif str(a[i][j])=='7':
            str+='seven'
        elif str(a[i][j])=='8':
            str+='eight'
        elif str(a[i][j])=='9':
            str+='nine'
        j=j+1
    i=i+1
    list1.append(str)
print(list1)