# A for loop is used itering over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

students = ['sonu', 'alekh', 'rashmee', 'chetan', 'sangram']

# Simple for loop

for person in students:
    print(f'current person: {person}')

# Break

for person in students:
    if person == 'rashmee':
        break
    print(f'current person: {person}')

#continue

for person in students:
    if person == 'rashmee':
        continue
    print(f'current person: {person}')    

# Range
for i in range(len(students)):
    print(students[i])

for i in range(0, 11):
    print(f'{i}')    

# While loops execute a set of statements as long as a condition is true.

count = 0
while count <= 20:
    print(f'count: {count}')
    count+=1

x=10
if x == 10:
    print(f'value is {x}')