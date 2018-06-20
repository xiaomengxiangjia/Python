def make_album(singer_name, album_name, num = ''):
    album = {'singer_name ': singer_name, 'album_name ': album_name}
    if num:
        album['num'] = num
    return album
    
album1 = make_album('caiyilin', 'kanwoqishierbian', num = 12)
album2 = make_album('zhoujielun', 'suanshenmenanren')
album3 = make_album('zhanghuimei', 'tinghai')
print(album1)
print(album2)    
print(album3)        
