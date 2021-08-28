a= [5, 6, [], 3, [], [], 9]
# print('actual list is'+str(a))
# # Remove empty List from List
# # using filter
# res = list(filter(None, a))
# print(res)
i=0
b=[]
while i<len(a):
    if a[i]!=[]:
        b.append(a[i])
    i=i+1
print(b)
#  Remove empty List from List        
# The original list is: [5, 6, [], 3, [], [], 9]
# List after empty list removal: [5, 6, 3, 9]
