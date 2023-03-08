# print('this is line one', end=" ")
# print('this is line two')

# print()
# print()

# word = 'commitment'
# letter = input('Please pick a letter: ')

# for n in word:
#     if n == letter:
#         print('_', end='')
#     else:
#         print(n.lower(), end='')

# print()
# print()



loop = True

while loop:
    number = int(input('Please give me a number. '))
    sent = 'This is going to be a really long sentance and I am going to keep this going forever and ever'

    for i, let in enumerate(sent):
        if (i % number):
            print(let.upper(), end="")
        else:
            print(let.lower(), end='')
    
