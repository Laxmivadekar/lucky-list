a= [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
i=0
c=0
d=0
e=0
f=[]
while i<len(a):
    if a[i]==4:
        c=c+1
    elif a[i]==6:
        d=d+1
    elif a[i]==4:
        e=e+1
if c>3 :
    f.append(c)
else:
    f.append(d)
print(f)
    




# Given a List, extract all elements whose frequency is greater than K.
# Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3
# Output: [4, 3]
# Explanation: Both elements occur 4 times.
# Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6], K = 2
