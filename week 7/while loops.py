# option = int(input('Would you like to:\n1) Go running\n2) Take a nap\n3) \
# Eat icecream\nOption(1-3):'))

# while option < 1 or option > 3:
#     print('Please print 1 2 or 3')
#     option = int(input('Would you like to:\n1) Go running\n2) Take a nap\n3) \
# Eat icecream\nOption(1-3):'))


# loki = True
# run = input('is he running? ')
# if run.upper() == 'YES':
#     loki = True
# else:
#     loki = False

# while loki == True:
#     print('Come back')
#     run = input('is he running? ')
#     if run.upper() == 'YES':
#         loki = True
#     else:
#         loki = False

# print('done')


word = 'LONG'
end_char = '.'
print(f'{word[2]}')
print(len(word))
i = 0
while i < len(word):
    # print(f'{word[i]}')
    print(word[i], end = end_char)
    i += 1

