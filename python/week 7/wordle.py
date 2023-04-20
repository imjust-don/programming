word = "windows"

guess = str(input('What is your guess? ').lower())

hint = ""
attempt = 1

while guess.lower() != word:
    print('That is incorrect')
    print('Your hint is ', "_ " * len(word) )
    print()
    attempt += 1
    guess = str(input('What is your guess? '))
print('')
print(f'That is correct! \nyou got it in {attempt} guesses!')
print()
