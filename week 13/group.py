def area_of_rectangle():
    print()
    first_side = float(input('What is the length of side one? '))
    second_side = float(input('What is the length of side two? '))

    area = first_side * second_side

    print()
    print(f"The area of your rectangle is {area}")
    return area

def area_of_square():
    print()
    side = float(input('What is the length of your square? '))

    area = side * side

    print()
    print(f"The area of your rectangle is {area}")
    return area


def area_of_triangle():
    print()
    base = float(input('What is the base of your triangle? '))
    height = float(input('What is the height of your triangle? '))

    area = (1/2) * base * height 

    print()
    print(f"The area of your rectangle is {area}")
    return area


def area_of_circle():
    print()
    radius = float(input('What is the radius of your circle? '))

    area = 3.14 * radius**2 

    print()
    print(f"The area of your rectangle is {area}")
    return area


quit = True

while quit:
    print('1. Square')
    print('2. Rectangle')
    print('3. Triangle')
    print('4. Circle')
    print('5. Quit')

    print()
    choice = int(input('What is your shape? '))

    if choice == 1:
        area_of_square()
        input()
    elif choice == 2:
        area_of_rectangle()
        input()
    elif choice == 3:
        area_of_triangle()
        input()
    elif choice == 4:
        area_of_circle()
        input()
    elif choice == 5:
        quit = False

