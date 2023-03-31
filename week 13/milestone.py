def wind_chill(temperature):
    count = 0
    wind_speed = 0.0
    while count <= 11:
        wind_speed += 5
        real_feel = 35.74 + (0.6215*temperature) - (35.75*(wind_speed**0.16)) + ((0.4275*temperature)*(wind_speed**0.16))
        print(f'At the temperature: {temperature}F, and the windspeed of: {wind_speed} MPH, the windchill is: {real_feel:.2f} Farenheit')
        count += 1


temp = float(input('What is the temperatur outside? '))
denomination = input('F or C? ')

real_temp = 0

if denomination.lower() == 'c':
    real_temp = ((9/5)*(temp)) + 32
elif denomination.lower() == 'f':
    real_temp = temp

wind_chill(real_temp)