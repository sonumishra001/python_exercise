name='sonu'
age=22

#concatenate
# print('my name is ' + name + ' and i am age' + str(age)) 

# #string formatting

# #arguments by position

# print('my name is {name} and i am {age}'.format(name=name, age=age))
#print(f'my name is {name} and i am {age}')
#String Methods

s='helloWORLD'
#Capitalize
print(s.capitalize())

# #UPPER CASE
print(s.upper())

#swap case
print(s.swapcase())

#ends with
print(s.endswith('d'))

#split into a list
print(s.split())

 
 #get length
print(s.__len__())

#replace
print(s.replace('WORLD', 'everyone'))

#count
sub='l'
print(s.count(sub))

#starts with
print(s.startswith('h'))

#ends with
print(s.endswith('D'))

#find position
print(s.find('R'))

#is all numeric
print(s.isnumeric())

#is all alphanumeric
print(s.isalnum())

#is all alphabetic
print(s.isalpha())