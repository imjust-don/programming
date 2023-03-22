choice = input('What would you like to learn more about? Old Testament, New Testament, Book of Mormon, Doctrine and Covenants, \nPearl of Great Price: ')

big = 'no'
big_book = ''
with open("books_and_chapters.txt") as data:
    for file in data:
        parts = file.strip().split(":")
        book = parts[0].strip()
        chapter = int(parts[1].strip())
        scripture = parts[2].strip()

        # if big == 'no' or big < chapter:
        #     big = chapter
        #     big_book = book

        if scripture.lower() == choice.lower() and (big == 'no' or big < chapter):
            big = chapter
            big_book = book

if choice.lower() == 'doctrine and covenants':
    print()
    print(f'The Doctrine and Covenants has 138 sections!')
    print()
else:
    print()
    print(f'The book with the most chapters in the {choice.title()} is {big_book.upper()} with {big} chapters!')
    print()