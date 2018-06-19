pets = ['dog', 'cat', 'dog', 'cat', 'goldfish', 'cat', 'rabbit', 'bird', 'mouse']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

for pet in set(pets):
    print(pet)
