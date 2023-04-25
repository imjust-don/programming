def main():
    start = float(input("What was your starting odometer reading? "))
    end = float(input("What was your endeing odometer reading? "))
    fuel = float(input("How many ganllons of fuel? "))

    mpg = miles_per_gallon(start, end, fuel)
    lpg = lp100k_from_mpg(mpg)

    print()
    print("---------------------------------")
    print(f"You got {mpg:.2f} miles per gallon")
    print(f"You got {lpg:.2f} litres per 100 kilometers")
    print("---------------------------------")
    print()

def miles_per_gallon(start, end, gallons):
    mpg = (end - start) / gallons

    return mpg

def lp100k_from_mpg(mpg):
    lpg = 235.215 / mpg

    return lpg

main()