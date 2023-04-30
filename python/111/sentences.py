import random

def main():
    x = 1
    print()
    while x <= 6:
        if x == 1:
            make_sentence(1, "past")
        if x == 2:
            make_sentence(1, "present")
        if x == 3:
            make_sentence(1, "future")
        if x == 4:
            make_sentence(2, "past")
        if x == 5:
            make_sentence(2, "present")
        if x == 6:
            make_sentence(2, "future")
        x += 1
    print()

def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    print(f"{determiner.capitalize()} {noun} {verb}.")


def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    word = random.choice(words)
    return word

def get_noun(quantity):
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    noun = random.choice(words)
    return noun

def get_verb(quantity, tense):
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    if tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    if tense == "present" and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    if tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    verb = random.choice(words)
    return verb
   

main()