# do_if = input('Should I do it? ')


# if do_if.lower() == 'yes':
#     print(f"Ok I'll do it")

# elif do_if.lower() == 'no':
#     print(f'Really you said no?')

# else:
#     print(f'Well what do you want me to do?')
print('')
print(f"Welcome to the Running decision maker")

temp = float(input('What is the temperature outside? '))

if temp >= 55:
    if temp <= 65:
        rain = input('Is it raining outside? ')
        if rain.lower() == 'yes':
            if temp >= 65:
                print("You should go running")
            else:
                print("You should not go running")
        else:
            print(f"You should go running")
    else:
        print('You should go running')
else:
    print(f"You shouldn't go running") 
    print('') 

