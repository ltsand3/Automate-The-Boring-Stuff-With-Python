spam = ['ham', 'hamburger', 'pizza', 'fries']
empty = []

def letterSpace(x):
    y = x - 1

def commaSpace(x):
    y = (len(x) - 1)
    if x == []:
            return('This list is empty, try again')
    else:
        if x == 1:
            return(str(x[0]))
        for i in range(y):
            print(str(x[i]) + ', ', end = '')
        return('and ' + str(x[-1]))
    return commaSpace


print(commaSpace)
