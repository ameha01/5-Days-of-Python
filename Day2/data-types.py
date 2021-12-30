# Data types
# Numbers(int, float, complex)
# Int
# float
# Complex Number: 2 + 2j, 1 + 4j,
# Strings
# Booleans (True or Fals)
# List, Set, Tuple, Dictionary

# Builtin Function we use to check a type: type()

print(type(10))
print(type('10'))
print(type(9.81))
print(type(1 + 2j))

#Strings
# As short as a single character or as long as many pages

letter = 'a'
word = 'love'

print(letter)
print(len(letter))
print(word)
print(len(word))
print(word[0]) # index counting starts from 0, 1, 2, ..
print(word[2])
print(word [3])
last_index = len(word) - 1
print(word[last_index])
print(word[1:2]) # print word index from number 1 upto index number 2

sentence = 'I love Python.'

print(sentence)
print(sentence.upper())
print(sentence.lower())
print(sentence.count('love')) #counts the str
print(len(sentence))
last_index_2 = len(sentence) - 1
print(sentence[1])
print(sentence[last_index_2])

dna = '''gtggcgctgcagagtagaactccgttgttagaccagtaatatctgggggcggaagatggc
ctcggagcgaggctgaaggaactcagtatctaaaagttaattgatgagcatttctaccgg
ggagcgccgtagatggcagtgagccgtttaaagctcatcatctcagcaccgcgaagagtc
ctctgtgggggtccgggcacaccccgagtagtatcctgcacccaacacaggcatcccgtc
gagtatagtataaagaaggtctgcggttatttggtcctgttttctctttacgatacaacg
tataaaccgcgggcttgcagaagccatctcaatttaccttaccttcttcggtatattctt
tataggctggtcaacaacaatcaacattgggggtcgcgaaattcgtgacgccttaggccc
ttgcgtacaggacgttgttcttaccataattacaggctgacttgtgcgaaaagtccgatt
tgccacatgacactcctaccgagcagcttgcgttaggacagttcgcaaattccctaacaa
aggtagcgtttcggaagatacccaaagcggcgcaggtcttcccgaagcaaagtgtggccg
tgtggtgtacatggccacatgggaacagtcgagacgacgtctctcataagtagacggata
tgctatacttgcggcaggcaccagggttctattccggtatctttccgtgggggtgcattc
cgtccataggcctcgtcgccggggattaacggcggcttcgcccaccgttccattaagtgc
gcctatcggcatagaaggtcgtttcctagaaccgggtgctccctagttttacggactcca
tggatttgtatgggccacttgctattcgcgtaagggatcacatatggtttagagacccac
cggtgcaccaaaactcggccttcaagagcctgacaatttacatggctcacccttgtgacg
gtctagccgtagggctgaataacctcttttgcctaaacac'''

print(len(dna))

# find the percentage proportion of the words inside dna

total_count = len(dna)
a = dna.count('a')
c = dna.count('c')
g = dna.count('g')
t = dna.count('t')

print(a)
print(a, c, g, t)
print('Proportion:', a / total_count, c / total_count, g / total_count, t / total_count)
print('Proportion:', round(a / total_count, 2), round(c / total_count, 2), round(g / total_count, 2), round(t / total_count, 2))
print('Proportion:', 'a:', round(a / total_count * 100, 2), 'c:', round(c / total_count * 100, 2), 'g:', round(g / total_count * 100, 2), 't:', round(t / total_count * 100, 2))
print('Proportion:', 'a:', round(a / total_count * 100, 2), '%', 'c:', round(c / total_count * 100, 2), '%', 'g:', round(g / total_count * 100, 2), '%', 't:', round(t / total_count * 100, 2), '%')

# String methods
# .upper(), .lower(), .count()

sentence = 'I love Python and I love JavaScript. I am looking for a new job. I cannot wait to get start.'

print(sentence.count('I'))
print(sentence.count('I love'))

print(sentence.title)
print(sentence.swapcase())


# String Formatting

#The oldest way
country = 'Ethiopia'
city = 'Addis Ababa'

print('%s is in Africa.' %(country))
print('%s is in Africa. The Capital is %s' %(country, city))

gravity = 9.81
mass = 74
weight = mass * gravity


a = 4
b = 3
print(f'The sum of {a} and {b} is {a + b}.')
print(f'The difference of {a} and {b} is {a - b}.')
print(f'The product of {a} and {b} is {a * b}.')
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} x {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} ^ {b} = {a ^ b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')

first_name = 'Ameha'
last_name = 'Zewde'
country = 'USA'
city = 'New York'
skills = ['HTML','CSS','JS','Python']
age = 31
learn_lang = 'Python'
""" I am Asabeneh Yetayeh. I live in Helsinki, Finland. I teach Python. My skills are HTML, CSS, JS, and Python. I am 250 years old. """
print(f'I am {first_name} {last_name}. I live in {city}, {country}. I learn {learn_lang}. My skills are {skills}. I am {age} old.')
print(f'I am {first_name} {last_name}. I live in {city}, {country}. I learn {learn_lang}. My skills are {skills[0]}, {skills[1]}, {skills[2]} and {skills[3]}. I am {age} old.')

nums = [1, 2, 3, 4, 5, 6]
print(len(nums))
print(nums[0])
print(nums[1])
print(nums[4])
last_index = len(nums) - 1 # because index start counting the 1st index from 0
print(nums[last_index])
print(nums[:]) # slicing everythinh
print(nums[1:3]) # slicing between 2 & 4
print(nums[3:]) # left it black means upto the end

#negative
print(nums[-1])
print('lets check', nums[-3:-1]) # indexing doesn't include the last item
print(nums[-2:])

print(nums[0:-1]) # listing everything starting from zero upto one item before the last

print(','.join(['a', 'b', 'c'])) # to avoid the bracket of the lists
