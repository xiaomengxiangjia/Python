cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'audi':
        print(car.title() + ", I will buy it by myself.")
    elif car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
