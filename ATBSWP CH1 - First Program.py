createName = input('Create your username: ')
createNewPassword = input('Create your Password: ')

#name = input('Please enter your username') # Lines 4 and 5 previous design but new design is more aestetic
#password = input('Welcome back!')

print('Please Enter your username and passsword to login')
name = input('Enter your username: ')
if name == createName:
    print('Hello ' + name + '!')
    password = input('Please enter your password: ')
    if password == createNewPassword:
        print('Wassup, welcome back choom!')
    else:
        print('Wrong!')
