nums = list(range(1,6))
print(nums)

nums = [value ** 3 for value in range(1,11)]
print(nums)

nums = []
for values in range(1,11):
    nums.append(values ** 4)
print(nums)

players = ['a', 'b', 'c', 'd', 'e', 'f']
print(players[-3:])
players1 = players[:]
print(players1)

names = []
if names:
    for name in names:
        print("Hello " + name + ".")
    print("Welcome to university.")
else:
    print("We nees to find some users.")

current_users = ['jack', 'Rosie', 'nana', 'nancy', 'percy']
new_users = ['chenxiao', 'rosie', 'Percy', 'NaNcY', 'Zhanghan', 'HARRY']
for new_user in new_users:
    if new_user.lower() in [current_user.lower() for current_user in current_users]:
        print("Sorry " + new_user + " has been used.")
    else:
        print("Congratulations, you've got the name " + new_user + ".")
