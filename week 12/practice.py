
low_vote = 'empty'
flop = ''


with open("data.csv") as file:
    header = file.readline()
    for line in file:
        parts = line.strip().split(',')
        movie = parts[0].strip()
        votes = int(parts[1].strip())
        genera = parts[2].strip()


        if low_vote == "empty" or votes < low_vote:
            low_vote = votes
            flop = movie
            
            
print(f'Flop movie is {flop} with a votes of {low_vote}')



# for value in range(len(votes)):
#     if votes[value] >= 5:
#         print(f"{movie[value]} {votes[value]}")
