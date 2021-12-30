

empty_dict = dict() # {}
print(empty_dict)
print(type(empty_dict))


person = {
    'first_name': 'Ameha',
    'last_name':'Zewde',
    'country': 'Ethiopia',
    'city': 'Addis',
    'age':200,
    'is_married':True,
    'skills': ['Html', 'CSS', 'JS']
}

from pprint import pprint

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['skills'])
print(len(person['skills']))

person['nationality'] = 'Ethiopian' # we make additional dictionary for the person.
print(person['nationality'])
person['skills'].append('Python')


pprint(person)

person2 = person.copy()

