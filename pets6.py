def describe_pet(pet_name, animal_type = 'dog'):
    print("I have a " + animal_type + '.')
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet(pet_name = 'willie')    
describe_pet(pet_name = 'tiantian', animal_type = 'cat')    