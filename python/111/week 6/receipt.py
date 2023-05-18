import csv

def main():
    key_index = 0
    name_index = 1
    price_index = 2
    filename = "products.csv"
    file2 = 'request.csv'
    items = []

    products_dict = read_dictionary(filename, key_index)
    print(products_dict)
    print()
    print()
    print('Requested Items')
    with open(file2, 'rt') as request:
        reader = csv.reader(request)
        next(reader)
        for info in reader:
            item = info[0]
            thing = products_dict[item]
            price = thing[price_index]
            print(f'{thing[name_index]}: {info[1]} @ {price}')
            items.append(info)



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
