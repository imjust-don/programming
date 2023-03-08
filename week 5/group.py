grade = int(input('What is the grade percentage: '))
letter = 'A'

if grade >=90:
    letter = "A"
elif grade >=80:
    letter = 'B'
elif grade >=70:
   letter = "C"
elif grade >=60:
    letter = 'D'
elif grade <60:
    letter = 'F'

plus = "+"
minus = "-"

if letter == 'A' or letter == 'F':
    if grade % 10 > 3 or grade == 100:
        print(f'Your grade is an {letter}')
        print('')
    elif grade % 10 <= 3:
        if letter == 'A':
            print(f'Your grade is an {letter + minus}')
            print('')
        else:
            print(f'Your grade is an {letter}')
            print('')
    else:
         print(f'Your grade is an {letter}')
         print('')
else:
    if grade % 10 >= 7:
        print(f'Your grade is a {letter + plus}')
        print('')
    elif grade % 10 <= 3:
         print(f'Your grade is a {letter + minus}')
         print('')
    else:
         print(f'Your grade is a {letter}')
         print('')

if letter == "A" or letter == "B" or letter == "C" or letter == "D":
    print("You're doing great!")
else:
    print("Don't worry you can do this just focus.")
print('')



