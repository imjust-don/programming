cmeal = float(input("What is the price of an child meal? "))
ameal = float(input("What is the price of an adult meal? "))
child = int(input("How many kids are there? "))
adult = int(input("How many adults are there? "))
tax = float(input("What is the sales tax rate? "))
sub = (ameal * adult) + (cmeal * child)

print("---------------------")
print("")

print(f"Subtotal: ${sub}")

sales_tax = round(sub * (tax / 100), 2)

print(f"Sales Tax: ${sales_tax}")

total = sub + sales_tax

print(f"Total: ${total:.2f}")

print('')

tip = float(input('How much tip: '))

if tip == 0:
    
    paid = float(input('How much was paid?: '))

    print("")

    print(f'Change due: ${round(paid - total, 2)}')

    print("")
    print("----------------------")

else:
    total_tip = total + tip

    print(f"Total with tip: ${total_tip:.2f}")
    
    print("")

    paid = float(input('How much was paid?: '))

    print("")

    print(f'Change due: ${round(paid - total_tip, 2)}')

    print("")
    print("----------------------")
