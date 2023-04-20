temp_f = float(input('What is the temperature in farenheit: '))

temp_c = (temp_f - 32) * (5/9)

if temp_c == 0:

    print(f'The temperature in Celcius is {temp_c:.0f}')
    # This makes it so that if the temperatur is 0 then it prints '0' instead of '0.0'

else:
    print(f'The temperature in Celcius is {temp_c:.1f}')