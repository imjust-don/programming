print("")

age = input("What is your age? ")

birthday = int(age) + 1

print("")

print("Oh cool that means on your next birthday you'll be" + " " + str(birthday))

print("")

print("")

eggs = int(input("How many cartons of eggs do you have? "))

print("")

print(f"You have {eggs * 12} eggs.")

print("")
print("")

people = int(input("How many people are there? "))
print("")
cookies = int(input("How many cookies are there? "))
print("")


if cookies // people == 1:
    print(f"That means each person will get {cookies // people} cookie. ")
else:
    print(f"That means each person will get {cookies // people} cookies. ")

print("")
