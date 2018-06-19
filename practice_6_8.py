dogs = {'type': 'tydde', 'owner': 'xiaojie'}
cats = {'type': 'us', 'owner': 'xiaozhang'}
birds = {'type': 'normal', 'owner': 'afei'}
pets = [dogs, cats, birds]
for pet in pets:
    print(pet['owner'].title() + "'s pet is a type of " + pet['type'].title() 
        + ".")
    
