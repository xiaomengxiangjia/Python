class Resturant():
    def __init__(self, resturant_name, cuisine_type):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type
     
    def describe_resturant(self):
         print("The resturant's name is " + self.resturant_name.title() + ".")
         print("The cuisine type is " + self.cuisine_type + ".")
         
    def open_resturant(self):
         print(self.resturant_name.title() + " is opening.")  

my_resturant = Resturant('Delicious', 'cooking')
print("The resturant's name is " + my_resturant.resturant_name.title() + ".")
print("The cuisine type is " + my_resturant.cuisine_type.title() + ".")

my_resturant.describe_resturant()
my_resturant.open_resturant()

class IceCreamStand(Resturant):
    def __init__(self, resturant_name, cuisine_type):
        super().__init__(resturant_name, cuisine_type)
        self.favor = ['cool', 'sugar', 'nice']
        
    def describe_icecreamstand(self):
        for n in self.favor:
            print("My favorite taste is " + n.title() + ".")
        
my_icecream = IceCreamStand('A', 'B')
my_icecream.describe_icecreamstand()

