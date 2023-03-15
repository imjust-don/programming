choice = 0
cart = []
item = 0
count = 0
cost = []
print('Welcome to the shopping cart program')

while choice != 5:
    print()
    print("""Please select one of the following: 
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit""")
    
    choice = int(input("Please enter an action: "))

    if choice == 1:
        item = input('What would you like to add to your cart? ')
        cart.append(item)
        price = float(input('What is the price? '))
        cost.append(price)
    if choice == 2:
        print('The content of your cart is: ')
        print()
        for i in range(len(cart)):
            print(f'{i + 1}. {cart[i]} - ${cost[i]}')
        print()
        input()
    if choice == 3:
        print('The content of your cart is: ')
        print()
        for i in range(len(cart)):
            print(f'{i + 1}. {cart[i]} - ${cost[i]}')
        print()
        remove = int(input('What would you like to remove? '))
        removed_item = cart.pop((remove - 1))
        removed_cost = cost.pop((remove - 1))
        print()
        print(f'Ok we will remove {removed_item} for ${removed_cost}')
    if choice == 4:
        print('The content of your cart is: ')
        print()
        for i in range(len(cart)):
            print(f'{i + 1}. {cart[i]} - ${cost[i]}')
        print('-----------------------')
        print(f'Your total is ${sum(cost):.2f}')
        print('-----------------------')
input()

