import math
items = int(input("Enter the number of items: "))
in_box = int(input("Enter the number of items per box: "))

boxes = math.ceil(items / in_box)

print()
print(f"For {items} items, packing {in_box} items in each box, you will need {boxes} boxes.")
print()