word = "windows"



hint = ""
attempt = 1
guessed = False
print('Your hint is:', '_ ' * len(word))
while guessed == False: 
    print()
    guess = str(input('What is your guess? ').lower())
    if guess == word:
        print(f"Thats correct the word is {word.upper()} you got it in {attempt} guesses")
    elif len(guess) < len(word) or len(guess) > len(word):
        print(f'Please only enter {len(word)} letters')
    else:
        print('That is incorrect')
        print()
        print('Your hint is:', end=' ')
        for n ,let in enumerate(word):
            if let == guess[n]:
                print(f"{let.upper()}", end=' ')
            else:
                print("_", end=' ')
    attempt += 1
    if guess == word:
        guessed = True
    else:
        guessed = False


