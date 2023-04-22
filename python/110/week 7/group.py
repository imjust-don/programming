import random
play = "yes"
while play.lower() == 'yes':
    # magic = int(input('What is the magic number? '))
    magic = random.randint(1, 10)
    print("---------------------------------------------")
    print("Guess a number 1-10 to find the magic number!")
    print("---------------------------------------------")

    attempt = 1

    guess = int(input('Whats your guess? '))

    if magic > guess:
        print()
        print('Higher')
    elif magic < guess:
        print()
        print('Lower')

    while magic != guess:
        guess = int(input('Whats your guess? '))
        attempt += 1
        print(f'This is guess number {attempt}')
        if magic > guess:
            print()
            print('Higher')
        elif magic < guess:
            print()
            print('Lower')

    print("--------------------------------------")
    print(f"Good job the magic number is {magic}!")
    print("--------------------------------------")

    play = input('Would you like to play again? ')

    while play.lower() != 'yes' and play.lower() != 'no':
        play = input('Would you like to play again? (yes or no) ')


print()
print('Thanks for playing!')
print()