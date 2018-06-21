def cars(manufacturer, model, **car_info):
    cars_info = {}
    cars_info['manufacture: '] =  manufacturer
    cars_info['model: '] = model
    for key, value in car_info.items():
        cars_info[key] = value
    return cars_info
    
cars_detail = cars('china', 'suv',
    color = 'blue',
    tow_package = 'True')
print(cars_detail)
