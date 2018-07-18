a = input("Please input your name: ")
print(a.title())

filename = 'guest.txt'

with open (filename, 'w') as  file_project:
    file_project.write(a.title())
