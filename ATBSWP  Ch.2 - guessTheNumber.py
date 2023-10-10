#This is a guess the number game.

import random

#Generates Random Number
secretNumber = random.randint(1,20)
print('Choose a number between 1 and 20. You have six chances to guess the correct number!')

#Gives thge Player six chances to Input Random Number

for guessesTaken in range(1,7):
    print('Take a guess')
    playerNumber = int(input())

    if playerNumber < secretNumber:
        print('Your guessed ' + str(playerNumber) + ' That is too low. Try again!')
    elif playerNumber > secretNumber:
        print('Your guessed ' + str(playerNumber) + ' That is too high. Try again!')
    else:
        break #The player guessed correctly


#Compares the computers number to the players input and determines if there was a match

if secretNumber == playerNumber:
    print('You win! It took you ' + str(guessesTaken) + ' tries to guess my number.')
else:
    print('You lose! ' + 'The number that I had in mind was ' + str(secretNumber))


