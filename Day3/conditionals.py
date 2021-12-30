a = 0

'''if a > 0:
    print('It is positive')
elif a == 0:
    print('The value is zero')
elif a < 0:
    print('then it is negative')
else:
    print('we dont know about this number')'''

if a > 0:
    print(f'{a} is a positive number')
elif a == 0:
    print(f'{a} is zero')
elif a < 0:
    print(f'{a} is negative')
else:
    print('we dont know about this number')
'''
weather = input('what is the weather like today?')

if weather == 'rainy':
    print('pls take umberella')
elif weather == 'cloudy':
    print('It is good to consider taking umberella')
elif weather == 'shiny':
    print('the day seems great go out freely')
elif weather == 'snowy':
    print('It might be slepper')
elif weather == 'foggy':
    print('there might be limited visibility')
else:
    print('No one know the weather')
'''



'''He is Asabeneh Yetayeh. He is 250 years old. He live in Helsink, Finland. '''

first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
year_born = int(input('When were you born '))
current_year = 2021
country = input('where are you from? ' )
city = input('what is the capital city? ')
gender = input('What is your gender ? ').lower()

pronoun = ''
if gender == 'female'.lower() or gender == 'f'.lower():
    pronoun = 'She'
elif gender == 'male'.lower() or gender == 'm'.lower():
    pronoun = 'He'
