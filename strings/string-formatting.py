first_name = 'Santiago'
last_name = 'Cortez'

#Different methods for formatting strings
# output = 'Hello ' + first_name + ' ' + last_name
# output = 'Hello {} {}'.format(first_name, last_name)
# output = 'Hello {1}, {0}'.format(first_name, last_name)
output = f'Hello, {first_name} {last_name}'
print(output)