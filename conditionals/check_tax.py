price = float(input('How much did you pay?\n'))
if price >= 1.00:
    tax = .07
else:
    tax = 0    
print(f'Tax rate is {str(tax)}')
