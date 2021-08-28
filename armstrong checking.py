n=[153,164,370,371,384,407,454]
i=0
sum=0 
temp=n
while i<len(n):
    if n[i]>0:
        rem=temp%10
        sum+=rem**3
        temp//=10
    i=i+1
if temp==n[i]:
    print('it is Armstrong',n[i])
else:
    print('it is not Armstrong',n[i])