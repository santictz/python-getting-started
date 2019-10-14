country = input('What country do you live in?\n')
province = input('What province do you live in?\n')

if country.lower() == 'canada':
    if province in ('Alberta' 'Nunvaut', 'Yukon'):
        tax = 0.05
    elif province == 'Ontario':
        tax = 0.13
    else:
        tax = 0.15
else:
    tax = 0
