createName = input('Create your username: ')
createNewPassword = input('Create your Password: ')

#name = input('Please enter your username') # Lines 4 and 5 previous design but new design is more aesthetic
#password = input('Welcome back!')
print('')
print('Thanks for creating a new account! Confirm your membership by logging in.')

print('')

name = input('Enter your username: ')
while name != createName:
    name = input('Try again: ')
    if name == createName:
       break
print('Hello ' + name + '!')


password = input('Please enter your password: ')
while password != createNewPassword:
    #else:
    password = input('Wrong password please check your credentials: ')
    if createNewPassword == password:
     break
print('Welcome, choom!')



