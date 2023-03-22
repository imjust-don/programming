count = 0
biggest = 'no'
biggest_year = ''
place = ''
small = 'no'
small_year = ''
small_place = ''
with open("milestone\\life-expectancy.csv") as data:
    header = data.readline()
    for thing in data:
        stuff = thing.strip().split(',')
        entity = (stuff[0].strip())
        code = (stuff[1].strip())
        year =(stuff[2].strip())
        exactancy = float(stuff[3].strip())

        if biggest == 'no' or biggest < exactancy:
            biggest = exactancy
            biggest_year = year
            place = entity

        if small == 'no' or small > exactancy:
            small = exactancy
            small_year = year
            small_place = entity

print()
print(f'The overall max life expectancy is: {biggest} from {place} in {biggest_year}')
print(f'The overall min life expectancy is: {small} from {small_place} in {small_year}')
print()


# max = max(exactancy)
# min = min(exactancy)

# for i in range(len(exactancy)):
#     if exactancy[i] == max:
#         print(f'The overall max life expactancy is: {exactancy[i]} from {entity[i]} in {year[i]}')
#     if exactancy[i] == min:
#         print(f'The overall minimum life expactancy is: {exactancy[i]} from {entity[i]} in {year[i]}')

# print()
# print(f'max = {max}')
# print(f'min = {min}')

