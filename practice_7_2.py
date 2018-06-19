message = input("How many people you have? ")
message1 = int(message)
if message1 < 9:
    print("Ok, I will give you a desk of " + str(message1) + ".")
else:
    print("Sorry, we don't have a desk of " + str(message1) + ".")
    
