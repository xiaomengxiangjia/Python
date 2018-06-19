response = {}
answer_active = True
while answer_active:
    name = input("\nWhat's your name?")
    answer = input("If you could visit one place in the world ,where would you go?")
    
    response[name] = answer
    
    repeat = input("Would you like to introduce the activity to others?yes or no ")
    if repeat == 'no':
        answer_active = False
    
print("------The answer is------")
for name,answer in response.items():
    print(name.title() + " Would like to visit " + answer.title() + ".")
