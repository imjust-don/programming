num1 = int(input('Can you give me a number? '))
num2 = int(input('How about a second? '))

print('')

if num1 > num2:
    print(f'The first number is bigger than the second')
elif num1 == num2:
    print(f'The two numbers you have given me are equal')
else:
    print(f"The second number is bigger than the first")
print('') 


my_animal = "Flying Fox"
user_animal = input('What is your favorite animal? ')

print('')

if user_animal.upper() == my_animal.upper():
    print(f"Wow thats my favorite animal too!")
elif user_animal.upper() == 'BAT':
    print(f"Wow thats cool! I like bats to. My favorite \
    animal is a Flying Fox the biggest type of bat")
else:
    print('Thats cool I like Bats. Specifically the Flying Fox the biggest bat there is')

print('')