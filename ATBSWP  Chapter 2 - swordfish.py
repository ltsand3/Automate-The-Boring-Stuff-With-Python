while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print("Hello, Joe. What's the password?(Hint: It is a fish.)")
    password = input()
    while password != 'Coy':
        password = input('Wrong try again:')
    if password == 'Coy':
        print('In there like swimwear!')
        break

