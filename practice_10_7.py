print("Give me two numbers, I will add them.")
print("Press 'q' to quit.")

while True:
    first_number = input("First number:\n")
    if first_number == 'q':
        break
    second_number = input("Second number:\n")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        pass
    else:
        print("The sum of two is " + str(answer) + ".")

