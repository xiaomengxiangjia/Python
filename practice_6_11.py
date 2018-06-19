cities = {
    'chengdu': {'country': 'china', 'population': 1604, 'fact': 'many beauties'},
    'london': {'country': 'uk', 'population': 828, 'fact': 'delicious tea with milk'},
    'washington':{'country': 'us', 'population': 68, 'fact': 'fried chicken'},
}
for name,speciallys in cities.items():
    print(name.title() + " belongs to " + speciallys['country'].title() + ", population is " +
        str(speciallys['population']) + " ten thousand,the feature is " + speciallys['fact'] + ".")
