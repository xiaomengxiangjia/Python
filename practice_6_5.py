rivers = {
    'nile': 'egypt',
    'yellow river': 'china',
    'Mississippi River': 'us',
    }
for name,country in rivers.items():
    print("The " + name.title() + " runs through " + country.title() + ".")

for name in rivers.keys():
    print(name.title())
    
for country in rivers.values():
    print(country.title())
