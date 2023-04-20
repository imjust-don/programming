def get_income():
    income = float(input("What was your income for this week? "))
    return income

def compute_tithe(income):
    tithe = 0.1 * income
    return tithe



# amount = float(input('What was your income this week? '))

# print(compute_tithe(amount))

# print(compute_tithe(float(input("what is your income this week? "))))

print(compute_tithe(get_income()))


def ask_yes_or_no(prompt, affirmative = 'YES', negative = "NO"):
    response = ''
    while response != affirmative.upper() and response != negative.upper():
        response = input(f'{prompt} ({affirmative.upper()}/{negative.upper()}) ').upper()
        if response == affirmative.upper():
            return True
        elif response == negative.upper():
            return False
        else:
            print("PLease enter valid response")


is_raining = ask_yes_or_no('Is it going to rain?', 'you bet')

if is_raining:
    print('Don\'t go running')
else:
    is_snowing = ask_yes_or_no('Is is snowing?', negative='nada')
    if is_snowing:
        print('Dont\'t go running')
    else:
        print('Maybe you should go running')