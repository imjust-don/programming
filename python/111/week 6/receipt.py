import csv
from datetime import datetime

def main():
    key_index = 0
    name_index = 1
    price_index = 2
    filename = "products.csv"
    file2 = 'request.csv'
    items = []
    total = 0

    products_dict = read_dictionary(filename, key_index)
    print(products_dict)
    print()
    print()
    print('Inkom Emporium')
    print()

    with open(file2, 'rt') as request:
        reader = csv.reader(request)
        next(reader)
        for info in reader:
            quant = int(info[1])
            item = info[0]
            thing = products_dict[item]
            price = float(thing[price_index])
            total = total + (quant * price)
            print(f'{thing[name_index]}: {info[1]} @ {price}')
            items.append(int(info[1]))


    current_date_and_time = datetime.now()
    print()
    print()
    print(f"Number of items: {sum(items)}")
    print(f"Subtotal: {total :.2f}")
    print(f"Sales Tax: {(total * .06) :.2f}")
    print(f"Total: {(total + (total * .06)) :.2f}")
    print('Thank you for shopping at the Inkom Emporium.')
    print(f"{current_date_and_time:%A %I:%M %p}")



def read_dictionary(filename, key_column_index):

    dictionary = {}
    
    with open(filename, 'rt') as my_file:
        reader = csv.reader(my_file)
    
        next(reader)
        for line in reader:

            key = line[key_column_index]

            dictionary[key] = line

    return dictionary


main()
