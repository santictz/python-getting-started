santiago = {}
santiago['first'] = 'Santiago'
santiago['last'] = 'Cortez'
#Dictionary
susan = {'first' : 'Susan', 'last': 'Ibach'}
#List
people = [santiago, susan]
people.append({'first': 'Bill', 'last': 'Gates'})

print(people)
#Select a range from the list
presentors = people[0:2]
print(presentors)
#Obtain the lenght of the list
print(len(presentors))