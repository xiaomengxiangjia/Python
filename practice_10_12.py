import json

def get_number():
    """如果存储了数字，则获取它"""
    filename = 'number.json'
    try:
        with open(filename) as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return number
        
def show_number():
    """指出用户最喜欢的数字"""
    number = get_number()
    if number:
        print("I konw your favorite number,it's " + number + "!")
    else:
        number = input ("Enter your favorite number: " )
        filename = 'number.json'
        with open(filename, 'w') as f_obj:
            json.dump(number, f_obj)
            print("I know your favorite number, it's " + number + "!")
            
show_number()
