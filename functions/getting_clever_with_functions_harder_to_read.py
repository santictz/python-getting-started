# This function will take a name and return the
# first letter of the name
def get_initial(name, force_uppercase=True):
    if force_uppercase:
        return name[0:1].upper()
    else:
        return name[0:1]

# Ask for someone's name and return it's initials
first_name = input('Enter your first name:\n')
middle_name = input('Enter your middle name:\n')
last_name = input('Enter your last name:\n')
#named notations
print(f'Your initials are {get_initial(first_name, False)} {get_initial(force_uppercase=True, first_name=middle_name)} {get_initial(last_name, False)}')