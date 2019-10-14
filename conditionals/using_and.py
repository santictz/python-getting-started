# A student makes honour roll if their avergar is >= 85
# and their lowest grade is not below 70
gpa = float(input('What was your Grade Point Average?\n'))
lowest_grade = float(input('What was your lowest grade?\n'))

if gpa >= .85 and lowest_grade >= .70:
    print('You made the honour roll')