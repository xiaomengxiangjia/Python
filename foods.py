my_foods = ['pizza', 'falafel', 'carrot cake', 'beer', 'chicken']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('icecream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friends's favorite foods are:")
print(friend_foods)

print("The first three items in the list are:" )
print(my_foods[:3])


print("The items from the middle of the list are:" )
print(my_foods[1:4])


print("The last three items in the list are:" )
print(my_foods[-3:])

for my_food in my_foods:
	print(my_food)

for friend_food in friend_foods:
	print(friend_food)
