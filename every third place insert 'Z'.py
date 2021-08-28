a= ['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']
# b=a
# c=b
# a.insert(3,'Z')
# b.insert(7,'Z')
# c.insert(11,'Z')
# print(c)

# Original list:
# ['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']
# Insert Z in said list after every 3 th element:
# ['s', 'd', 'f', 'Z', 'j', 's', 'a', 'Z', 'j', 'd', 'f', 'Z', 'd']
i=3
while i<len(a):
    a.insert(i,'Z')
    i=i+4
print(a)