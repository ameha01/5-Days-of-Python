from pprint import pprint
empty_dict = dict() # {}
print(empty_dict)
print(type(empty_dict))

user = {
    'first_name':'John',
    'last_name':'Doe'
}

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'country':'Finland',
    'city':'Helsinki',
    'age':250,
    'is_married':True,
    'skills':['HTML', 'CSS','JS']
}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['skills'])
print(len(person['skills']))

person['nationality'] = 'Ethiopian'
person['skills'].append('Python')
print(person['nationality'])
person['hobbies'] = ['Jogging','Bikking']

pprint(person)

person['age'] = 70

if 'hobbies' in person:
    print('HIS BOBBIES', person['hobbies'])


print(person.get('first_name'))
print(person.get('schools'))

keys = person.keys()
print(keys)

print(person.values())
print(person.items())
print(len(person))
for key in person:
    print(key, ":", person[key])


print('nationality' in person)
print('email' in person)
person.clear()
del person
print(person)

person2 = person.copy()