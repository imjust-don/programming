sales = float(input('How much was the sale for: '))

commision = float(input('How much commision did you earn (%): '))

sales_rounded = round(sales, 2)

print(f'${sales:,.2f}')
# the ',' makes it add a comma every thousands place so your numbers look right and the .2 is rounding the number to the 100th place
# and the f states that we are working with the floating point (how we use numbers it represents our floating point decimal system)
# you can put an 'e' instead of the 'f' and it would return scientific notation (4.23e+10) as apposed to (4.23)

print('or with rounding you get')

print(f'{sales_rounded:,}')
commision_earned = sales * commision / 100
print(f'Commision earned will be ${commision_earned:,.2f}')