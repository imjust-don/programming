account = []
balance = []

loop = True
while loop:
    type = input('What is the account type? ')
    if type.lower() == 'quit':
            loop = False
    else:
        account.append(type)
        amount = float(input('What is the balance? '))
        balance.append(amount)

print('Account information')
print('--------------------')
for info in range(len(account)):
     print(f'{account[info]} - ${balance[info]}')

print()
average = sum(balance) / len(balance)
print(f'Sum: ${sum(balance)}')
print(f'Average: ${average:.2f}')


highest = max(balance)

for high in range(len(balance)):
     if highest == balance[high]:
        print(f'Highest balance: {account[high]} - ${balance[high]}')
print('--------------------')

loop = True
while loop:
        update = input('Would you like to update an account? ')


        if update.lower() == 'yes':
                for i in range(len(account)):
                        print(f'{i}. {account[i]}')

        print()
        update = int(input('Which account would you like to update? '))

        for i in range(account):
                if i == update:
                        new_amount = int(input('What is the new amount? '))
                        balance[i] = new_amount
                for i in range(len(account)):
                                print(f'{i}. {account[i]}')
        else:
               loop = False

for i in range(len(account)):
        print(f'{i}. {account[i]}')