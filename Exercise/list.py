# A List is a collection which is ordered and changable. Allows duplicate members.
#Create List

numbers=[1, 2, 3, 4, 5]
fruits=['apple', 'oranges', 'grapes', 'banana']

#Use a constructor
#numbers2= list((1, 2, 3, 4, 5))

#print(numbers, numbers2)

print(fruits[2])

#get length
print(len(fruits))

#append to list
fruits.append('mangoes')
print(fruits)

#remove from list
fruits.remove('banana')
print(fruits)

#insert into position
fruits.insert(2, 'strawerries')
print(fruits)

#remove from position 
fruits.pop(2)
print(fruits)

#reverse list
fruits.reverse()
print(fruits)

#sort list
fruits.sort()
print(fruits)

#reverse sort
fruits.sort(reverse=True)
print(fruits)

#change value
fruits=['apple', 'oranges', 'grapes', 'banana']
fruits[0] = 'black berry'
fruits.insert(0, 'papaya')
fruits.pop(1)

print(fruits)
print(len(fruits))