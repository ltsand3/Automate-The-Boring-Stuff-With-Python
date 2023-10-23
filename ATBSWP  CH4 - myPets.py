myPets = ['Zophie', 'Pooka', 'Fat-Tail']
print('Enter a pet Name.')
name = input()
while name not in myPets:
        print('I do not have a pet named ' + name + '!')
        print('Try a different name.')
        name = input()
print('This is ' + name + '!')
