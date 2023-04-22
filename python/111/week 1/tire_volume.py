from datetime import datetime
import math

print()
width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect = int(input("Enter the aspect ratio of the tire (ex 60): "))
diamater = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = (math.pi * width**2 * aspect * (width * aspect + 2540 * diamater))/10000000000

print()
print(f'The approximate volume is {volume:.2f} liters')
print()

file_object = open('volumes.txt', 'a')

file_object.write(f"\n{datetime.now()}, {width}, {aspect}, {diamater}, {volume:.2f}")

file_object.close()
