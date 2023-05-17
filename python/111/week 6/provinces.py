

def main():
    count = 0
    provinces = read_file("provinces.txt")
    print(provinces)

    for item in provinces:
        if item == "Alberta":
            count += 1
    print()
    print(f"The number of times Alberta appears in this list is {count}")


def read_file(filename):
   
    with open(filename, 'rt') as info:
        list = []

        for item in info:
            clean = item.strip()

            if clean.upper() == "AB":
                clean = "Alberta"
                list.append(clean)
            else:
                list.append(clean)

    return list
            
main()