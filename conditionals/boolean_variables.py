gpa = float(input('What was your Grade Point Average?\n'))
lowest_grade = float(input('What was your lowest grade?\n'))

if gpa >= .85 and lowest_grade >= .70:
    honour_roll = True
else:
    honour_roll = False
# somewhere later in your code if you need to check if students is 
# on honour roll, all I need to do is check the boolean variable
# I set earlier in my code
if honour_roll:
    print('You made honour roll')
