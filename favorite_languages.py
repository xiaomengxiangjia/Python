favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'pyhton',
    }
print(favorite_languages)
print("Sarah's favorite language is " +
    favorite_languages['sarah'].title() +
    ".")

for name,language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

for name in favorite_languages.keys():
    print(name.title())

for name in favorite_languages:
    print(name.title())
