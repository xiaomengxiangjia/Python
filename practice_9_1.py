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
my_resturant.describe_resturant()
my_resturant.open_resturant()
