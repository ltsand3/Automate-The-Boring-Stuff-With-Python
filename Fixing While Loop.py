#Changing the annoying while loop lesson to a loop that can be resolved.

name = ''
answer = ''
while name == '':
    print('Please type your name.')
    name = input()
    print('Is your name correct?')
while answer != 'yes':
    answer = input()
    if answer == 'yes':
        print('Thanks ' + str(name) +'!')
    else:
        print('Please re-enter your name.')
