def show_magicians(names):
    for name in names:
        print("The magician is " + name.title() + ".")
        
def make_great(names):
    while names:
        current_magician = "The Great " + names.pop()
        current.append(current_magician)
  
magician_names = ['lisa', 'bella', 'robbin']
current = []
make_great(magician_names)
show_magicians(current)
    

