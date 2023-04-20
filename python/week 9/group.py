numbers = []

print('Please enter some numbers input 0 when done: ')
user = -1

while user != 0:
    user = int(input('Enter a number: '))
    numbers.append(user)

del numbers[len(numbers) - 1]
print(f'The sum of your numbers is {sum(numbers)}')
print(f'The max number is {max(numbers)}')
print(f'Th smallest number you entered is {min(numbers)}')
print(f'The average of your numbers is {sum(numbers) / len(numbers)}')

numbers.sort()

print(numbers)

