class Resturant():
    def __init__(self, resturant_name, cuisine_type):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type
        self.number_saved = 0
     
    def describe_resturant(self):
         print("The resturant's name is " + self.resturant_name.title() + ".")
         print("The cuisine type is " + self.cuisine_type + ".")
         
    def open_resturant(self):
         print(self.resturant_name.title() + " is opening.") 
         
    def saving_number(self):
        print("There are " + str(self.number_saved) + " person had lunch here.")

    def set_number_saved(self, people):
        self.number_saved = people
        
    def increment_number_served(self, person):
        self.number_saved += person

my_resturant = Resturant('Delicious', 'cooking')
print("The resturant's name is " + my_resturant.resturant_name.title() + ".")
print("The cuisine type is " + my_resturant.cuisine_type.title() + ".")

my_resturant.describe_resturant()
my_resturant.open_resturant()

my_resturant.saving_number()

my_resturant.number_saved = 18
my_resturant.saving_number()

my_resturant.set_number_saved(20)
my_resturant.saving_number()

my_resturant.increment_number_served(50)
my_resturant.saving_number()
