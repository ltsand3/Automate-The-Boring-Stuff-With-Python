def spam():
    global eggs
    eggs = '2 eggs '
    bacon = '2 slices of bacon and '
    print(bacon + eggs)

eggs = 'globa1'
spam()
print(eggs)
