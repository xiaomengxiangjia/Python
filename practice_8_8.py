def make_album(singer_name, album_name):
    full_name = singer_name + ',' + album_name
    return full_name.title()
    
while True:
    print("\nPlease tell me the singer_name:")
    print("enter 'quit' at any time to quit.")
    
    sing_name = input("Singer_name:")
    if sing_name == 'quit':
        break
    
    albu_name = input("Album_name:")
    if albu_name == 'quit':
        break
        
    final_name = make_album(sing_name, albu_name)
    print("\nThe album you choose is : " + final_name + "!")
