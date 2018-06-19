sandwich_orders = ['apple sandwish', 'banana sandwish', 'pear sandwish']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made you " + current_sandwich)
    finished_sandwiches.append(current_sandwich)

for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche)
