from collections import OrderedDict

explain = OrderedDict()

explain['in'] = 'right here'
explain['not in'] = 'not here'
explain['rstrip'] = 'delete right space'
explain['lstrip'] = 'delete left space'

for name, explaination in explain.items():
    print(name.title() + " means " + explaination.title() + ".")
