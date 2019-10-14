#To get current date we need to import datetime library
from datetime import datetime

current_date = datetime.now()
#The now function returns current date and time as a datetime object

#You must convert the datetime object to string
#before you can concatenate it to another string
print(f'Today is {str(current_date)}')