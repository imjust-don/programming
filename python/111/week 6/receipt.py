import csv

def main():
    key_index = 0
    name_index = 1
    price_index = 2

    products_dict = read_dictionary('products.csv', key_index)
    print(products_dict)



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
