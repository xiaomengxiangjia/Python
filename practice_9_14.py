from random import randint

class Die():
    def __init__(self):
        self.sides = 6
    
    def roll_die(self, num):
        self.num = num
        """创建骰子面数为num"""
        x = randint(1,num)
        print(x)
        
my_try = Die()
"""当骰子面数为6"""
my_try.roll_die(6)        
my_try.roll_die(6)
my_try.roll_die(6)
my_try.roll_die(6)
my_try.roll_die(6)
my_try.roll_die(6)
my_try.roll_die(6)
my_try.roll_die(6)
my_try.roll_die(6)
my_try.roll_die(6)
print("---------------------")

"""当骰子面数为10"""
my_try.roll_die(10)
my_try.roll_die(10)
my_try.roll_die(10)
my_try.roll_die(10)
my_try.roll_die(10)
my_try.roll_die(10)
my_try.roll_die(10)
my_try.roll_die(10)
my_try.roll_die(10)
my_try.roll_die(10)
my_try.roll_die(10)
print("---------------------")

"""当骰子面数为20"""
my_try.roll_die(20)
my_try.roll_die(20)
my_try.roll_die(20)
my_try.roll_die(20)
my_try.roll_die(20)
my_try.roll_die(20)
my_try.roll_die(20)
my_try.roll_die(20)
my_try.roll_die(20)
my_try.roll_die(20)

