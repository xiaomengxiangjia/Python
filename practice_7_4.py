message = "Please input something you like:"
message += "\nInput 'quit' to end."

while True:
    message1 = input(message)
    if message1 == 'quit':
        break
    else:
        print("We'd like to add " + message1 + " into your pizza.")


