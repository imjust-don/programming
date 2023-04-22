number = int(input('Write a number lower than -1: '))

while number >= -1:
    print()
    number = int(input('Write a number lower than -1: '))
print()
print(f"Thank you. You entered the number {number}")

print('')
candy = input('Can I have some candy? ')

while candy.upper() != 'YES':
    print('')
    candy = input('Can I have some candy? ')

print()
print('Thank you')