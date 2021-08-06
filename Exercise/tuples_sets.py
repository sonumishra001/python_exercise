# A Tuple is a collection which is ordered and unchangable. Allows duplicate members.

#Create Tuple
from typing import get_args

#you can add duplicate value when creating tuple not after using add()
fruits = ('apple', 'apple', 'Oranges', 'Grapes')
#fruits2 = tuple(('apple', 'Oranges', 'Grapes'))

#Single value needs trailing comma
fruits2 =('Apple',)


print(fruits)
#Get Value
print(fruits[1])

#Can't chnage value
#fruits[0] = 'peers'

#delete tuple
# del fruits2
# print(fruits2)

print(len(fruits))

#A Set is a collection which is unordered and unindexed. No duplicate members.

#Create a Set

fruit_set = {'apple', 'Oranges', 'Grapes'}
print(fruit_set)

#Check if in set
print('apple' in fruit_set)

#Add to set
fruit_set.add('banana')
print(fruit_set)

#remove from set
fruit_set.remove('banana')
print(fruit_set)

#clear set entirely
# fruit_set.clear()
# print(fruit_set)

#delete set
# del fruit_set
# print(fruit_set)


#cant add duplicate data
fruit_set.add('apple')
print(fruit_set)
