# movies = [
#     'interstellar',
#     'up',
#     'batman',
#     'killer',
# ]
# x = 1
# print(movies)
# # prints the list

# for movie in movies:
#     print(f'-{movie.title()}')

# movies.append('iron man')

# for movie in movies:
#     print(f'{x}. {movie.title()}')
#     x += 1
x = 0
selection = 0
selections = []
menu = [
'1 - Drink',
'2 - Entree',        
'3 - Side',
'4 - Dessert',
'5 - Order complete'
    ]
drinks = [
    'water',
    'orange juice',
    'Root beer',
    'lemonade'
]
entree = [
    'hamburger',
    'cheeseburger',
    'hotdog',
    'nachos'
]

while selection != 5:
    print()
    for item in menu:
        print(f' {item}')
    print()


    selection = int(input('What would you like to order? '))
    print(f'You selected {selection}')


    if selection != 5:
        selections.append(selection)
    
    if selection == 1:
        x += 1
        for order in drinks:
            print(f"{x} - {order}")
print()
print()

for order in selections:
    print(f'You ordered a {order}')