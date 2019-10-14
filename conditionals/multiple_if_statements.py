province = input('What province do you live in?\n')
tax = 0
#You can use the OR and IN statement
if province in ('Alberta', 'Nunvatun', 'Yukon'):
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15

print(tax)