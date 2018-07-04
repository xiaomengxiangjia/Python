class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
        
    def show_privileges(self):
        print(self.privileges)
        
class Admin():
    def __init__(self, first_name, last_name):
        self.privileges = Privileges()
        
user = Admin('bin', 'li')
user.privileges.show_privileges()
