word = 'secret'


# for x in word:
#     print(x)

# print()

# i = 0
# while i < len(word):
#     print(word[i])
#     i += 1

# for letter in word:
#     print(word)
# total = 0
# for x in range(len(word)):
#     letter = word[x]
#     print(f"{x} - {letter}")
# print('-------------------------')
# for y in range(0, 100, 2):
#     print(y)
#     total = total + x
# print(total)
import random
letters = "abcdefghijklmnopqrstuvwxyz"
for row in range(len(word)):
    for col in range(len(word)):
        if row == col:
            print(word[row], end = " ")
        else:
            print(random.choice(letters), end = ' ')
    print()

print()
print()

if 's' in word:
    print('s is found')
else: 
    print('s is not found')

for i in range(len(word)):
    letter = word[i]