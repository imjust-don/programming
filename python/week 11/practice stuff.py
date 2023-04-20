
# .strip()

test_string = '\ttest\n'

print(test_string)
print(test_string.strip())

# .split()

split_test = 'This is a really, long test sentance'

print(split_test.split())
print(split_test.split(','))
# hi

# data = [
#     'Pizza, 1',
#     'peporoni, 2',
#     'French fries, 3'
# ]
total = 0
with open("data.csv") as data:
    header = data.readline()
    for entry in data:
        items = entry.split(',')
        food = items[0]
        # print(food.title())
        qty = int(items[1].strip())
        total += qty
        print(f'{food} - {qty}')
print(f'Your total is ${float(total)}')