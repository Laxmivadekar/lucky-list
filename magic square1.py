magic=[[8,3,4],[1,5,9],[6,7,2]]
i=0
r1=0
r2=0
r3=0
c1=0
c2=0
c3=0
d1=0
d2=0
while i<len(magic):
    c1=c1+magic[0][i]
    c2=c2+magic[1][i]
    c3=c3+magic[2][i]
    d1=d1+magic[i][i]
    d2=d2+magic[i][2-i]
    j=0
    while j<len(magic[i]):
        if i==0:
            r1=r1+magic[i][j]
        elif i==1:
            r2=r2+magic[i][j]
        elif i==2 :
            r3=r3+magic[i][j]

        j=j+1
    i=i+1
if r1==r2==r3==c1==c2==c3==d1==d2:
    print('magic square')
else:
    print('not magic square')
i=i+1