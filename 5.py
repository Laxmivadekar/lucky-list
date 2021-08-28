# i=-4
# end=5
# a=[]
# while i<=end:
#     a.append(i)
#     i=i+1
# print(a)
#
a=[-4,-3,-2,-1,0,1,2,3,4,5]
j=0
c=[]
d=[]
while j<len(a):
    if a[j]<0:
        c.append(a[j])
    else:
        d.append(a[j])
    j=j+1
print(c)









# Input: start = -4, end = 5
# Output: -4, -3, -2, -1

# Input: start = -3, end = 4
# Output: -3, -2, -1
