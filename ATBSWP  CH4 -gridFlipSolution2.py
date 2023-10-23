#import copy didn't need a deepcopy because we didnt need to reference changes to the grid.

#Based on the problem we need to print the rotate the grid list of list
# 90 degrees clockwise.

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


#for x in range(6): #Thought I needed a for loop but the program only needed to be ran once using a while loop! :)
#flippedGrid = copy.deepcopy(grid)

column = []
xCoord = 0 # starting x coordinate for the bottom of the list
yCoord = 0 # starting y coordinate for first column we're transposing
xCoord2 = xCoord + 1 #Variable used to continue while loop


while xCoord <= 8 and yCoord <=5:
    column.append(grid[xCoord][yCoord])
    print(''.join(column), end = '')
    xCoord += 1

    column = [] # Clears the column once a single value is entered so each list item is printed seperately.
    #print(xCoord, yCoord, end = ' '), - here I printed the X and Y values to test the selection.

    if xCoord  > 8 :
        print('', sep = '')
        yCoord += 1
        xCoord -= 9
        #print(xCoord, yCoord), - Checked the value before returning to the while loop





