filename = 'practice_name.txt'
with open (filename, 'w') as file_object:
    while True:
        name = input("Please input your name, press 'quit' to quit!\n")
        if name == 'quit':
            break;
        else:
            file_object.write("Hello, " + name.title() + "." + '\n')
