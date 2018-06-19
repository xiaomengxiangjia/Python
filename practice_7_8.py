sandwish_orders = ['fish sandwish', 'sarah sandwish', 'vegetables sandwish']
finished_sandwishes = []

while sandwish_orders:
    current_sandwish = sandwish_orders.pop()
    print("I made you " + current_sandwish.title() + ".")
    finished_sandwishes.append(current_sandwish)

print("\nThe following sandwishes have been made:")
for finished_sandwish in finished_sandwishes:
    print(finished_sandwish.title())
    
