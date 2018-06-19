favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for languages in favorite_languages.values():
    print(languages.title())
    
for languages in set(favorite_languages.values()):
    print(languages.title())
