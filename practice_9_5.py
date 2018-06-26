class User():
    def __init__(self, first_name, last_name,user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info
        self.login_attempts = 0
        
    def describe_user(self):
        print("The " + self.first_name.title() + self.last_name.title() + 
            "'s address is " + self.user_info.title() + ".")
    
    def greet_user(self):
        print("Hello, " + self.first_name.title() + ' '
            + self.last_name.title() + ".")
            
    def increment_login_attempts(self):
        self.login_attempts += 1
            
    def reset_login_attempts(self):
        self.login_attempts = 0
            
user_first = User('chen', 'chen', 'chengdu')
user_second = User('bin', 'bin', 'yaan')
user_third = User('fan', 'fan', 'ziyang')

user_first.describe_user()
user_second.describe_user()
user_third.describe_user()

user_first.greet_user()
user_second.greet_user()
user_third.greet_user()
         
print("login_attempts:", user_first.login_attempts)
user_first.increment_login_attempts()
print("login_attempts:", user_first.login_attempts)
user_first.increment_login_attempts()
print("login_attempts:", user_first.login_attempts)
user_first.reset_login_attempts()
print("login_attempts:", user_first.login_attempts)
