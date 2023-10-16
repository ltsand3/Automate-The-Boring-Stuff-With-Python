import time, sys
indent = 0 #how many space to indent
indentIncreasing = True #Whether the indentation is incrasing or not

try:
    while True: #The main program loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) #pauses for 0.1(1/10) of a second

        if indentIncreasing:
            #Increase the number of spaces
            indent = indent + 1
            if indent == 20:
                #change direction:
                indentIncreasing = False

        else:
            #Decrease the number of spaces
            indent = indent -1
            if indent ==0:
                # change direction:
                indentIncreasing = True
except KeyboardInterrupt:
        sys.exit()

