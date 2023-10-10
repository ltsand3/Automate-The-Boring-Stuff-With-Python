createName = input('Create your username: ')
createNewPassword = input('Create your Password: ')

#name = input('Please enter your username') # Lines 4 and 5 previous design but new design is more aesthetic
#password = input('Welcome back!')

print('Thanks for creating a new account! Confirm your membership by logging in.')
name = input('Enter your username: ')
if name == createName:
    print('Hello ' + name + '!')
    password = input('Please enter your password: ')
    if password == createNewPassword:
        print('Welcome, choom!')
    else:
        print('Wrong!')


