playerone=input('enter the name')
playertwo=input('enter the name')
if playerone==playertwo:
    print('tie')
elif playerone=='rock' and playertwo=='paper':
    print('playertwo was won the match')
elif playerone=='rock' and playertwo=='seassor':
    print('playerone was won the match')
elif playerone=='paper' and playertwo=='rock':
    print('playerone was won the match')
elif playerone=='paper' and playertwo=='seassor':
    print('playertwo was won the match')
elif playerone=='seassor' and playertwo=='rock':
    print('playertwo was won the match')
elif playerone=='seassor' and playertwo=='paper':
    print('playerone was won the match')        
