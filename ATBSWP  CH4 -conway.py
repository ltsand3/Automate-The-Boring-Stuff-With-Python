# Conway's Game of Life
import random, time, copy
WIDTH = 60
HEIGHT = 20

# Create a list of list for the cells
nextCells = []
for x in range(WIDTH):
    column = [] #Create a new column
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#') #add a living cells
        else:
            column.append(' ') #Add a dead cell
    nextCells.append(column) #next cells is a list of column lists

while True: #Main program loop
    print('\n\n\n\n\n') #Separate each step with newlines.
    currentCells = copy.deepcopy(nextCells)

    #Print currentCells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')#print the #(living cells) or ' '(dead cells)
        print() # print a new line at the end of the row

    #Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            #Get neighboring coordinates:
            #'% WIDTH' ensure leftCoordoord is always between 0 and WIDTH - 1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

        #Count number of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-left neighbor is alive.
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-right neighbor is alive.
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 #Right neighbor is alive.
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 #Bottom-right neighbor is alive.
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 #Bottom neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 #Bottom-left neighbor is alive.
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 #Left neighbor is alive.


        #Set cell based on Cnway's Game of Life Rules:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or
        numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                #Dead cells with neighbors come alive
                nextCells[x][y] = '#'
            else:
                #everything dies or is already dead
                nextCells[x][y] = ' '
    time.sleep(1)

