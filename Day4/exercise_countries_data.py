# import countries_data
# find ten most populated countries
# china, indie, usa, ...

from countries_data import countiries_info
from pprint import pprint
""" for c in countiries_info:
   # print(c)
    print(c['name'], c['capital'], c['population'], len(c['languages']))
 """
populations = []
for c in countiries_info:
    populations.append(c['population'])

#sorting
pprint(sorted(populations))
pprint(sorted(populations, reverse=True))

sorted_coutries = sorted(populations, reverse=True
top_ten_countries = sorted_countries[:10]
print(top_ten_countries)