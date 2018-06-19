message = "Please input your age:"
message += "\nInput 'quit' if you want to end."

active = True
while active:
    message1 = input(message)
    if message1 == 'quit':
        break
    elif int(message1) < 3:
        print("You are free.")
    elif int(message1) < 12:
        print("You need to pay $10.")
    else:
        print("You need to pay $15.")

