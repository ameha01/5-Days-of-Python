# functions: is to do some purpose.
# there are two types of function
# 1) builtin function: print(), len(), type(), max(), min(), sum(), 
# 2) custom function: that we create functions
# String Method: .split(), .count()
# custom function: we usually use ['def' name_of_func '():'] then it will create 'block'.
def name_of_func ():
    print('This is a funct and its is name_of_func')

name_of_func ()

def xyz ():
    print('I am a function')
xyz()

def do_something():
    print('I am doing something') #in order to run & get result you have to call it the name below
do_something()

def get_person_info ():
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
    return f'{pronoun} is {first_name} {last_name}. {pronoun} is {current_year - year_born} years old. {pronoun} live in {country}, {city}.'

# print(get_person_info())
 


def rectangel_area (l,w):
    area = l * w
    return area # you can also say [f'{area} square meter']

# print(rectangel_area(1, 3))

def perimeter_rectangel (l, w):
    perimeter = 2 * (l +  w)
    return perimeter

# print(perimeter_rectangel(1, 4))

def generate_even(n):
    evens = list(range(0, n + 1, 2))
    return evens

# print(generate_even(50))

def generate_odd(n):
    odds = list(range(1, n + 1, 2))
    return odds

# print(generate_even(50))

def rectangel_area ():
    l = float(input('L: '))
    w = float(input('W: '))
    area = l * w
    return area # you can also say [f'{area} square meter']

# print(rectangel_area())

def calc_weight (mass, gravity = 9.81): # it's possible to pass default value by parameters
    weight = mass * gravity
    return weight

# print(calc_weight(75))


