filename = 'reasons.txt'
with open (filename, 'a') as file_project:
    while True:
        questions = input("Why you like to program? press 'quit' to quit.\n")
        if questions == 'quit':
            break;
        else:
            file_project.write(questions + "\n")
