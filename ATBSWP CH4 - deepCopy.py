import copy

spam = ['A', 'B', 'C', 'D']
spam.append(['E', 'F', 'G', 'H'])
print(id(spam))

cheese = copy.deepcopy(spam)
print(id(cheese))

cheese[1] = 42
print(spam)
print(cheese)

# Write your code here :-)
