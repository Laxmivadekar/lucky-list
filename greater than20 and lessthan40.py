n=[50,40,23,70,56,12,5,10,7]
length=len(n)
index=0
morethan20=0
lessthan40=0
while index<length:
    marks=n[index]
    if marks>20:
        morethan20=morethan20+1
    else:
        lesstha40=lessthan40+1
    index+=1
print('morethan20: ')
print('lesstha40: ')