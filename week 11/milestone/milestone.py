

choice = input('Enter your year of interest ')


biggest = 'no'
biggest_year = ''
place = ''
small = 'no'
small_year = ''
small_place = ''
year_list = []

biggest2 = 'no'
place2 = ''
small2 = 'no'
small_place2 = ''
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

        if year == choice:
            year_list.append(exactancy)

            if biggest2 == 'no' or biggest2 < exactancy:
                biggest2 = exactancy
                biggest_year2 = year
                place2 = entity

            if small2 == 'no' or small2 > exactancy:
                small2 = exactancy
                small_year2 = year
                small_place2 = entity

average = sum(year_list) / len(year_list)



print()
print(f'The overall max life expectancy is: {biggest} from {place} in {biggest_year}')
print(f'The overall min life expectancy is: {small} from {small_place} in {small_year}')
print()


print()
print(f'For the year {choice}')
print()
print(f'The average life expactancy for all countries is {average}')
print(f'The max life expectancy was in {place2} with {biggest2}')
print(f'The min life expectancy was in {small_place2} with {small2}')
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

