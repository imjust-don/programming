r1a = int(input('What is the age of the first rider: '))
r1h = int(input('What is the height of the first rider: '))
if r1h < 36:
    print('Sorry you cant ride.')
else:
    r2 = input('Is there another rider (y/n): ').lower()
    r2h = 0
    r2a = 0

    ride = r1a + r2a

    golden = False

    if r1h < 36:
        print('Sorry you cant ride.')
    else:
        if r2 == ('y'):
            r2h = int(input('What is the second riders height: '))
            r2a = int(input('What is the second riders age: '))
        elif (r1a >= 12 or r2a >= 12) and r2h >= 52:
            print("You're good to ride!")
        elif (r1a <= 12 or r2a <= 12) or r2h <= 52:
            print('Sorry you cant ride.')
        elif r2h < 36:
            print('Sorry you cant ride.')
        elif (r2 == 'n') and (r1a < 18 or r1h < 62) and golden == False:
            print('Sorry you cant ride.')
        else:
            print("You're good to ride!")