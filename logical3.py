i=1
while i<=20:
    n=int(input('enter a number'))
    if n>0:
        print(n,'it is positive number')
    if n<0:
        print(n,'it is negative number')
    if n%2==0:
        print(n,'it is even')
    if n%2!=0:
        print(n,'it is odd')
    if n==0:
        print(n,'is equal to zero')
    i=i+1