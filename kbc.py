a=['what has a head,a tail but not have abody','bey of bengal in which state','what is always coming and not arrives']
b=[['coin','belt','snake','bottle'],['solid','liquid','constant','kolkata'],['today','air','tomorrow','water']]
c=[1,2,3]
f=[['coin','belt'],['solid','liquid'],['today','tomorrow']]
fs=[1,2,2]
i=0
count=0
while i<len(a):
    print('these are your',i+1,'question')
    print(i+1,a[i])
    print('these are your options')
    j=0
    while j<len(b[i]):
        print(j+1,b[i][j])
        j=j+1
    n=int(input('enter a number: '))
    if n==c[i]:
        print('congratulations....')
    elif n==5050:
        if count==0:
            k=0
            while k<len(f[i]):
                print(k+1,f[i][k])
                k=k+1
            count=count+1
            n1=int(input('select your options'))
            if n1==fs[i]:
                print('right answers.......')
            else:
                print('your answer is wrong')
                break
        else:
            print('sorry you are already used')
            n2=int(input('select your optionss'))
            if n2==c[i]:
                print('congratulations.....')
            else:
                print('wrong answer')
                break
    else:
        print('wrong answer you can quit your game')
        break
    i=i+1