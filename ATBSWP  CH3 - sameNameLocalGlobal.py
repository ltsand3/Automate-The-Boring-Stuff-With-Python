def spam():
    global eggs
    eggs = 'spam' #this is the global

def bacon():
    eggs = 'bacon' #This is local

def ham():
    print(eggs) #this is global

eggs = 42 # this is global
spam()
print(eggs)
