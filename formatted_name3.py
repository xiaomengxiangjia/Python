def get_formatted_name(first_name, middle_name, last_name):
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()
    
musician = get_formatted_name('john', 'lee', 'hooker')
musician1 = get_formatted_name('john', 'james', 'hooker')
print(musician)
print(musician1)
 
