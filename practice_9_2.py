class Resturant():
    def __init__(self, resturant_name, cuisine_type):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type
     
    def describe_resturant(self):
         print("Tht resturant's name is " + self.resturant_name.title() + ".")
         print("Tht cuisine type is " + self.cuisine_type.title() + ".")
         
    def open_resturant(self):
         print(self.resturant_name.title() + " is opening.")  

my_resturant = Resturant('Convenient', 'fried')
my_resturant1 = Resturant('Cheap', 'stew')
my_resturant2 = Resturant('HEALTH', 'BOIL')

my_resturant.describe_resturant()
my_resturant1.describe_resturant()
my_resturant2.describe_resturant()


