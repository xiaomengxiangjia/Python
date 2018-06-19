favorite_places = {
    'xiaofu': ['paris','america','china'],
    'xiaobin': ['beijing','europe'],
    'xiaoli': ['chengdu', 'luzhou', 'europe'],
}
for name,places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places are: ")
    for place in places:
        print("\t" + place.title())
