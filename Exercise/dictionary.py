# A Dictionary is a collection which is unordered, changable and indexed. No duplicate members
#Create a Dictionary

person = {
    'first_name': 'sonu',
    'last_name': 'mishra',
    'age': 22
}

#use a constructor
# person2= dict(first_name='edith', last_name='jackson')
# print(person2, type(person2))

#get value
print(person['first_name']) 
print(person.get('last_name'))

#add key/value
person['phone'] = '8456030514'
print(person)

#get keys
print(person.keys())
#get items
print(person.items())

#copy a dictionarty
person2 = person.copy()
person2['city']='bhubaneswar'
print(person2)

#remove an item
del(person2['age'])
print(person2)

person2.pop('phone')
print(person2)

#Clear
# person2.clear()
# print(person2)

#get length
print(len(person2))

#list of dict
people =[
    {'name': 'ajay', 'age': 24},
    {'name': 'rahul;', 'age': 26}
]

print(people)
