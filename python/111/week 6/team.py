import csv


def main():
    Id_index = 0
    NAME_INDEX = 1
    students_dict = read_dictionary("students.csv", Id_index)

    inumber = input("Please enter an I-Number (xx-xxx-xxxx): ")


    inumber = inumber.replace("-", "")


    if not inumber.isdigit():
        print("Invalid character in I-Number")
    else:
        if len(inumber) < 9:
            print("Invalid I-Number: too few digits")
        elif len(inumber) > 9:
            print("Invalid I-Number: too many digits")
        else:

            if inumber not in students_dict:
                print("No such student")
            else:

                value = students_dict[inumber]
                name = value[NAME_INDEX]

                print(name)


def read_dictionary(filename, key_column_index):

    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # From the current row, retrieve the data
            # from the column that contains the key.
            key = row_list[key_column_index]

            # Store the data from the current row
            # into the dictionary.
            dictionary[key] = row_list


    return dictionary

main()