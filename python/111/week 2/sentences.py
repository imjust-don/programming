import random

def main():
    x = 1
    print()
    while x <= 6:
        if x == 1:
            get_prepositional_phrase(1)
        if x == 2:
            get_prepositional_phrase(1)
        if x == 3:
            get_prepositional_phrase(1)
        if x == 4:
            get_prepositional_phrase(2)
        if x == 5:
            get_prepositional_phrase(2)
        if x == 6:
            get_prepositional_phrase(2)
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

def get_preposition():
    word = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    thing = random.choice(word)
    return thing

def get_prepositional_phrase(quantity):
    prep = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    print(f"{prep.capitalize()} {determiner} {noun}.")


main()

