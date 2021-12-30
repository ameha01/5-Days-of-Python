# Strings
String = 'It is anything inside a sing or double qoate'
letters = 'abcdefghijklmnopqrstuvwxyz0123456789'
print(len(letters))
#Slice
print(letters[0])
print(letters[-1])

#different string methods
program = 'five days of Python'
sentences = 'I love people. Love is the great thing. I love Java and Pyhton. There is nothing like love.'

print(len(program))
print(program.upper())
print(program.lower())
print(program.title())
print(program.split(' '))
print(sentences.count('love'))
print(sentences.lower().count('love'))
print(sentences.split(' ')) 
print(sentences.replace('.',' '). split(' ')) # in orde to remove the 'dot' which included with the sentence closing words (in the upper code/ check the result)

