information0 = {'first_name': 'rose', 'last_name': 'Deep', 'age': 24, 
    'city': 'NewYork'}
information1 = {'first_name': 'lily', 'last_name': 'dwtson', 'age': 18, 
    'city': 'america'}
information2 = {'first_name': 'jack', 'last_name': 'dwtson', 'age': 19, 
    'city': 'us'}
peoples = [information0, information1, information2]        
for people in peoples:
    full_name = people['first_name'] + " " + people['last_name'] 
    print(full_name.title() + "'s age is " + str(people['age']) + ", who lives in "
        + people['city'].title() + ".")
