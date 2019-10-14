from datetime import datetime, timedelta

birthday = input('When is your birthday? (dd/mm/yyy)\n')
#Parse string to date using a specific format
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')

print(f'Birthday {str(birthday_date)}')

one_day = timedelta(days=1)
birthday_eve = birthday_date - one_day
print(f'Day before your birthday: {str(birthday_eve)}')
