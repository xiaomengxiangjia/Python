def city_country(city_name, country):
    countries = city_name + ', ' + country
    return countries.title()
    
city_country1 = city_country('santiago', 'chile')
city_country2 = city_country('chengdu', 'china')    
city_country3 = city_country('beijing', 'china')
print(city_country1)
print(city_country2)
print(city_country3)
