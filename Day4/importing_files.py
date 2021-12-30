# import countries_list

# print(dir(countries_list))
# print(dir(countries_list.countries))
# print(countries_list.countries)
# from pprint import pprint
from countries_list import countries
from pprint import pprint

# pprint(countries)
""" 
new_list = []
for country in countries:
    new_list.append([country, country.upper(), country.upper()[:3], len(country)])
print(new_list)
pprint(new_list) """

def get_countries_with_is():
    new_list = []
    for c in countries:
        if 'ia' in c:
            new_list.append(c)
    return new_list

# print(get_countries_with_is())


def five_letter_countries():
    new_list = []
    for c in countries:
        if len[c] == 5:
            new_list.append(c)
    return new_list

print(five_letter_countries())


