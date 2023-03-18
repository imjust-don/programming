entity = []
code = []
year = []
exactancy = []
count = 0
with open("week 11\\milestone\\life-expectancy.csv") as data:
    header = data.readline()
    for thing in data:
        stuff = thing.split(',')
        entity.append(stuff[0])
        code.append(stuff[1])
        year.append(stuff[2])
        exactancy.append(stuff[3])


max = max(exactancy)
min = min(exactancy)

# for i in range(len(exactancy)):
#     if exactancy[i] == max:
#         print(f'The overall max life expactancy is: {exactancy[i]} from {entity[i]} in {year[i]}')
#     if exactancy[i] == min:
#         print(f'The overall minimum life expactancy is: {exactancy[i]} from {entity[i]} in {year[i]}')

print()
print(f'max = {max}')
print(f'min = {min}')

