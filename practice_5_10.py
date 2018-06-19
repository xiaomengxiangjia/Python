current_users = ['jack', 'Rosie', 'nana', 'nancy', 'percy']
new_users = ['chenxiao', 'rosie', 'Percy', 'NaNcY', 'Zhanghan', 'HARRY']
for new_user in new_users:
    if new_user.lower() in [current_user.lower() for current_user in current_users]:
        print("Sorry, " + new_user + " has been used,You need to input another name.")
    else: 
        print("Congratuation, " + new_user +" ,you have successfully registered.")
