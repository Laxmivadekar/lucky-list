a=[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
# b=a
# c=b
# d=c
# a.insert(4,20)
# b.insert(9,20)
# c.insert(13,20)
# d.insert(17,20)
# # print(a)
# # print(b)
# # print(c)
# print(d)

i=4
while i<len(a):
    a.insert(i,20)
    i=i+5
print(a)
# Original list:
# [1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
# Insert 20 in said list after every 4 th element:
# [1, 3, 5, 7, 20, 9, 11, 0, 2, 20, 4, 6, 8, 10, 20, 8, 9, 0, 4, 20, 3, 0]
# Original list:
# ['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']
# Insert Z in said list after every 3 th element:
# ['s', 'd', 'f', 'Z', 'j', 's', 'a', 'Z', 'j', 'd', 'f', 'Z', 'd']

