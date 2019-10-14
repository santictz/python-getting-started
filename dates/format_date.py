from datetime import datetime

today = datetime.now()

#use day, month, year, hour, minute second functions
#to display only part of the date
#All these functions returns integers
#Convert them to strings before concatenating them to another strings
print(f'Day: {str(today.day)}')
print(f'Month: {str(today.month)}')
print(f'Year: {str(today.year)}')
print(f'Hours: {str(today.hour)}')
print(f'Minute: {str(today.minute)}')
print(f'Seconds: {str(today.second)}')