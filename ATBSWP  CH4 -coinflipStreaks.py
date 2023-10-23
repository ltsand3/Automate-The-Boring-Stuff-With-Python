import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    headsTails = [] # Creates a global list to insert and interpret results.
    for i in range(100):
        if random.randint(0,1):   # Assigns a random int of 0 to 'h' or a 1 to 't' and appends the list.
            headsTails.append('h')
        else:
            headsTails.append('t')
#print(len(headsTails)) # Used to see if total values inserted into list = 100
# Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(100-6):
            if headsTails[i] == headsTails[i+1] == headsTails[i+2 ] == headsTails[i+3] == headsTails[i+4] == headsTails[i+5]:
                numberOfStreaks += 1
                break
print('The chance of streak every 100 flips is: %s%%' % (numberOfStreaks/100))



