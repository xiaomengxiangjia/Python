def describe_pet(pet_name, animal_type = 'dog'):
    print("I have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name + ".")
    
describe_pet('willie')    
describe_pet(pet_name = 'willie')

describe_pet('harry', 'hamster')
describe_pet('harry', animal_type = 'hamaster')
describe_pet(pet_name = 'harry', animal_type = 'hamaster')
describe_pet(animal_type = 'hamaster', pet_name = 'harry')
