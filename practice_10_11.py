import json

number = input("Enter your favorite number: " )
filename = 'number.json'
with open(filename, 'w') as f_obj:
    json.dump(number, f_obj)


