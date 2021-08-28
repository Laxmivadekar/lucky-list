pos_of_home=1
pos_of_at=5   #position of apple tree
pos_of_ot=-3   #position of orange tree
orange_fell_down=4
apples_fell_down=5
i=0
c=0
while i<=orange_fell_down:
    d=int(input('enter the direction of oranges')) #direction of oranges fell down
    p=d+pos_of_ot  #position of oranges
    if pos_of_home==p:
        c=c+1
    i=i+1
print('no. of oranges in home',c)
#it is for Apples
i=0
c=0
while i<=apples_fell_down:
    d=int(input('enter the direction of apples')) #direction of apples fell down
    p=d+pos_of_at  #position of oranges
    if pos_of_home==p:
        c=c+1
    i=i+1
print('no. of apples in home',c)