class User():
    def __init__(self, first_name, last_name,user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info
        
    def describe_user(self):
        print("The " + self.first_name.title() + self.last_name.title() + 
            "'s address is " + self.user_info.title() + ".")
    
    def greet_user(self):
        print("Hello, " + self.first_name.title() + ' '
            + self.last_name.title() + ".")
            
user_first = User('chen', 'chen', 'chengdu')
user_second = User('bin', 'bin', 'yaan')
user_third = User('fan', 'fan', 'ziyang')

user_first.describe_user()
user_second.describe_user()
user_third.describe_user()

user_first.greet_user()
user_second.greet_user()
user_third.greet_user()
         
class Admin(User):
    def __init__(self, first_name, last_name, user_info):
        super().__init__(first_name, last_name, user_info)
        self.privileges = ['can add post', 'can delete post', 'can ban user']
        
    def show_privileges(self):
        for privilege in self.privileges:
            print("Admin has privilege such as " + privilege + ".")
            
my_admin = Admin('zhenzhen', 'wen', 'female')
my_admin.show_privileges()
        
