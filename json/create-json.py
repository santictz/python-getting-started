import json

# Create a dictionary object
person_dict = {'first': 'Santiago', 'last':'Cortez'}
# Add additional key pairs to dictionary as needed
person_dict['city'] = 'Rosario'

# Convert dictionary to JSON object
person_json = json.dumps(person_dict)

# Print JSON
print(person_json)

# Add another dictionary
staff_dict = {}
staff_dict['Program Manager'] = person_dict

# Print JSON
print(json.dumps(staff_dict))

# Creates a list object and add it to the dictionary
languages_list = ['Csharp', 'Python', 'PHP']
person_dict['languages'] = languages_list
print(json.dumps(person_dict))