names = ['steve jobs', 'kristen stuwart', 'mom', 'dad', 'tuling']
print(names)

message0 = "\n Hello " + names[0] + ", can you have dinner with me?\n"
message1 = "Hello " + names[1] + ", can you have dinner with me?\n"
message2 = "Hello " + names[2] + ", can you have dinner with me?\n"
message3 = "Hello " + names[3] + ", can you have dinner with me?\n"
message4 = "Hello " + names[4] + ", can you have dinner with me?\n"
print(message0, message1, message2, message3, message4)

change_name = names.pop(1)
print(names)
print("I'm so sorry " + change_name + " can't have dinner with me .")

names.insert(1, 'robort pattson')
print(names)

for name in names:
	print("Thanks " + name + " for have dinner with me .")
	
message = "Hi everybody I have found a bigger place !\n\n"	
print(message) 

print(names)

names.insert(0, 'zhong')
print(names)

names.insert(3, 'huojin')
print(names)

names.append('yuan longping')
print(names)

for name2 in names:
	print("Hello " + name2 + ", welcome to my party !")
	
print("\n\nSorry everyone, I can only invite 2 of you .\n\n")

print(names)

names3 = names.pop(0)	
print("Sorry " + names3 + ", I will connect you soon .\n")
names4 = names.pop(0)
print("Sorry " + names4 + ", I will connect you soon .\n")
names5 = names.pop(0)
print("Sorry " + names5 + ", I will connect you soon .\n")
names6 = names.pop(0)
print("Sorry " + names6 + ", I will connect you soon .\n")
names7 = names.pop(-1)
print("Sorry " + names7 + ", I will connect you soon .\n")
names8 = names.pop(-1)
print("Sorry " + names8 + ", I will connect you soon .\n")
print(names)

for name9 in names:
	print("Hello " + name9 + ", I will be with you forever!\n")


print(names)

del names[0]  
print(names)

del names[0]
print(names)


len(names)
print("I invite " + str(len(names)) + " people with me to have dinner .")

















