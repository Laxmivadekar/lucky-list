r=0
while r<=3:
    c=0
    while c<=56:
        if ((r==0) and (c!=1 and c!=3 and c!=5 and c!=11 and c!=13 and c!=15 and c!=27 and c!=29 and c!=32 and c!=33 and c!=35 and c!=37 and c!=42 and c!=44 and c!=48 and c!=50 and c!=51 and c!=54)) or ((r==1) and (c!=1 and c!=4 and c!=7 and c!=10 and c!=15 and c!=17 and c!=21 and c!=23 and c!=25 and c!=27 and c!=29 and c!=31 and c!=34 and c!=36 and c!=38 and c!=40 and c!=43 and c!=45 and c!=47 and c!=49 and c!=51 and c!=53 and c!=55)) or ((r==2) and (c!=11 and c!=12 and c!=13 and c!=15 and c!=22 and c!=23 and c!=25 and c!=29 and c!=31 and c!=36 and c!=38 and c!=41 and c!=47 and c!=51 and c!=53 and c!=54 and c!=55)) or ((r==3) and (c!=1 and c!=4 and c!=7 and c!=8 and c!=10 and c!=11 and c!=15 and c!=21 and c!=23 and c!=25 and c!=27 and c!=29 and c!=32 and c!=34 and c!=36 and c!=38 and c!=40 and c!=43 and c!=47 and c!=49 and c!=51 and c!=52 and c!=53 and c!=55 and c!=56)):
            print('*',end=' ')
        else:
            print(end='  ')
        c=c+1
    print()
    r=r+1