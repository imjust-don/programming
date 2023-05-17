
import csv


def main():
    Id_index = 0
    name_index = 1

    students_dict = read_dictionary('students.csv', Id_index)
    inumber = input("Please enter an I-number (xx-xxx-xxxx): ")

    inumber = inumber.replace("-", "")

    if not inumber.isdigit():
        print("Invalid cahracter in I-number")
    else:
        if len(inumber) < 9:
            print("Invalid I-number: too few digits")
        elif len(inumber) > 9:
            print("Invalid I-number: Too many digits")
        else:

            if inumber not in students_dict:
                print("No such student")
            else:
                value = students_dict[inumber]
                name = value[name_index]

                print(name)


def read_dictionary(filename, key_column_index):

    dictionary = {} 

    with open(filename, "rt") as csv_file:

        reader = csv.reader(csv_file)
        next(reader)

        for row_list in reader:

            key = row_list[key_column_index]

            dictionary[key] = row_list

    return dictionary

main()