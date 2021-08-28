print('welcome to Andhra bank')
print('please enter your card')
print('1.Telugu')
print('2.English')
print('3.Hindi')
language=input('please select your language')
pin=int(input('please enter your pin number'))
print('1.withdraw/n','2.deposite/n','3.balance enquery/n','4.pin change/n','5.exit')
transaction=input('please select your transaction')
if (transaction=='1'):
    print('1.savings/n','2.current')
    type=int(input('choose account type: '))
    amount=int(input('please enter your amount'))
    if amount<=10000:
        print('wait a second for your cash')
    else:
        print('you dont have suffecient balance please try later')
if (transaction=='2'):
    deposite=int(input('please enter your deposited amount'))
    if deposite<=20000:
        print('your money successfully deposited')
    else:
        print('this money more than deposited limit')
if (transaction=='3'):
    receipt=(input('do you want receipt: '))
    if receipt=='yes':
        print('please collect your receipt')
    else:
        print('thank you for using....')
if (transaction=='4'):
    oldpin=int(input('enter your old pin'))
    if (oldpin==1234):
        newppin=input('do you want to change the pin')
    else:
        print('please enter a valid pin number')
else:
    print('enter valid old pin number')
if (transaction=='5'):
    print('Exit')
   
