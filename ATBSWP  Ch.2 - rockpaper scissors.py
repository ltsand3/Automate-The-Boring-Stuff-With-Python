# Rock, Paper, Scissors

import random, sys

wins = 0
losses = 0
ties = 0

print('ROCK, PAPER, SCISSORS')

while True: #Main game loop
    print ('%s Wins, %s Losses, %s Ties' %(wins, losses, ties))
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')

        playerChoice = input()
        if playerChoice == 'q':
            sys.exit() # Exit Program
        if playerChoice == 'r' or playerChoice == 'p' or playerChoice == 's':
            break #Breaks out of player input loop
        print('Type one of r,p,s,or q.')

    #Displays the Players move

    if playerChoice == 'r':
        print('ROCK versus...')
    elif playerChoice == 'p':
        print('PAPER versus...')
    elif playerChoice == 's':
        print('Scissors versus...')

    #Displays the computers choice

    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerChoice = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerChoice = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerChoice = 's'
        print('Scissors')

    #Displays Outcomes  of game

    if playerChoice == computerChoice:
        print('It is a tie')
        ties = ties + 1
    elif playerChoice == 'r' and computerChoice == 'p':
        print('Paper beats rock you lose!')
        losses = losses + 1
    elif  playerChoice == 'r' and computerChoice == 's':
        print ('Rock beats Scissors, you win!')
        wins = wins + 1
    elif playerChoice == 'p' and computerChoice == 's':
        print('Scissors beats paper you lose!')
        losses = losses + 1
    elif  playerChoice == 'p' and computerChoice == 'r':
        print ('Paper beats rock, you win!')
        wins = wins + 1
    elif playerChoice == 's' and computerChoice == 'r':
        print('Rock beats scissors, you lose!')
        losses = losses + 1
    elif  playerChoice == 's' and computerChoice == 'p':
        print ('Scissors beats paper, you win!')
        wins = wins + 1



#
