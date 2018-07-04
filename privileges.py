class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can ban user', 'can delete post']
    def show_privileges(self):
        print(self.privileges)
        
from admin import User
class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()
