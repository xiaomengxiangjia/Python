def foods(*names):
    for name in names:
        print("You ordered a " + name + " sandwish.")
foods('backon')
foods('friedchicken', 'vegetables')    
