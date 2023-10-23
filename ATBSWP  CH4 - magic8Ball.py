import random

messages = ['It is certain',
'It is decidedly so',
'yes definitely',
'Reply hazy try again',
'Ask again late',
'Concentrate and ask again',
'My reply is no',
'Outlook not so good',
'Very doubful',
]

print(messages[random.randint(0, len(messages)-1)])
