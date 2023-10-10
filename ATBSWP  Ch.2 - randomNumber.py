#This is a guess the number game.

import random

#Generates Random Number
secretNumber = random.randint(1,20)
print('Choose a Number Between 1 and 20. You have six chances to guess the correct number!')

#Gives thge Player six chances to Input Random Number

for guessesTaken in range(1,7):
    print('Take a guess')
    playerNumber = int(input())

    if playerNumber < secretNumber:
        print('Your guessed ' + str(playerNumber) + ' Thats too low. Try again!')
    elif playerNumber > secretNumber:
        print('Your guessed ' + str(playerNumber) + ' Thats too high. Try again!')
    else:
        break #The player guessed correctly

#Prints the players number and  computer number

print('You guessed in' +  ' ' )
print('The secret number is ' + str(secretNumber))

#Compares the computers number to the players input

if secretNumber == playerNumber:
    print('You win! It took you ' + str(guessesTaken) + ' tries to guess my number.')
else:
    print('You lose! ' + 'The number that I had in mind was ' + str(secretNumber))


