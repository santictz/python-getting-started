from datetime import datetime, timedelta

today = datetime.now()
print(f'Today is {str(today)}')

#You can use timedelta to add or remove days, or weeks to a date object
one_day = timedelta(days=1)
yesterday = today - one_day
print(f'Yesterday was {str(yesterday)}')

one_week = timedelta(weeks=1)
last_week = today - one_week
print(f'Last week was {str(last_week)}')