print('Welcome to the loan Calculator')
print('')

size = int(input('What amount are you seeking: '))
credit = int(input('What is your credit score: '))
income = float(input('What is your income: '))
payment = float(input('How much was your down payment: '))

if size >= 5:
    if (credit >= 7 and income >= 7) or ((credit >= 7 or income) and (payment >= 5)):
        print('Your loan is approved')
        print('')
    elif ((credit >= 7 or income) and (payment < 5)):
        print('Loan denied')
        print('')
    elif credit < 7 and income < 7:
        print('Loan denied')
        print('')
elif size < 5:
    if credit < 4:
        print('Loan denied')
        print('')
    elif (payment >= 7 or income >= 7) or (income == 4 and payment == 4):
        print('Loan aprroved')
        print('')
    else:
        print('Loan denied')
        print('')
