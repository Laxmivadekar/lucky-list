i=0
output=[]
while i<=6:
    command=input('enter a command')
    if command=='append':
        n=int(input('enter anumber'))
        output.append(n)
    elif command=='insert':
        index=int(input('enter the index'))
        n=int(input('enter a number'))
        output.insert(index,n)
    elif command=='sort':
        output.sort()
    elif command=='pop':
        output.pop()
    elif command=='remove':
        n=int(input('enter a number'))
        output.remove(n)
    elif command=='reverse':
        output.reverse()
    i=i+1
print(output)