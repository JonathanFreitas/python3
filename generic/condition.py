#Program test condition

name = str(input('Enter your name: '))

if(name == 'jhon'):
    password = int(input('Enter your password: '))
    if(password == 123):
        print('Welcome Mr. ', name)
    else:
        print('Permission denied')
else:
    print('Permission denied')