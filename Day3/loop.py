# loop - used to solve to make code shorter and facilitate repetitive works

# range(start, ende, incriment/step)

print(range(3)) # it generates numbers from 0 to 2
print(list(range(0,11))) # list from 0 to 11 but not includes 11 & default increment is '1'
print(list(range(10,100,10))) # list numbers from 10 to 100 by 10 increment

for num in [1,2,3,4,5]:
    print(num)           # taking out every items inside 'num' put in block.

for country in ['Ethiopia', 'Somalia', 'Kenya']:
    print(country)

for i in range(6): 
    print(i)        # range from 0 to 6 but not include 6
    print(f'{i} x {i} = {i ** 2}')

    students = ['Josh', 'Meski', 'Dawit', 'Mearege',  'Amaha', 'Tigist',  'Meron', 'Mirtsew']

for student in students:
    print(f'Hello {student}, \n Welcome to the Bootcamp. The bootcamp will be started on 26 December.')


for country in ['Ethiopia','Kenya','Somalia','Sudan', 'Finland','Ireland']:
    if 'land' in country:
        print(country)

for student in students:
    if len(student) > 5:
        print(student, 'You have got a long name')
    else:
        print(student,'You have got a short name')

total = 0
for i in range(0, 101, 2):
    total = total + i
print(total)

