import json


def generate_template_str(name, age):
    return f'Name: {name}, Age: {age}'


def generate_template_html(name, age):
    return f'''
<h1>{name}</h1>
<h2>{age}</h2>
'''


print(generate_template_str('Doncho', 23))
print(generate_template_html('Doncho', 23))

print(repr(json.loads('{"name":"Doncho"}')))
print(repr(json.dumps({'name': 'Doncho'})))
