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
xCoord = 8 # starting x coordinate for the bottom of the list
yCoord = 0 # starting y coordinate for first column we're transposing
xCoord2 = xCoord + 1 #Variable used to continue while loop


while xCoord >= 0 and yCoord <= 5: #and yCoord <=5:
    column.append(grid[xCoord][yCoord])
    #print(xCoord, yCoord, end = ' ')  #Used to test the selection of list items.
    xCoord = xCoord -1
    if xCoord  < 0:
        print(''.join(column))
        xCoord += xCoord2 #xCoordinate is -1 at the end of the loop need to add nine instead of 8 to ge to the bottom of the list.
        yCoord += 1 # moves to the next column
        column = [] #clears column so next line can be printed





