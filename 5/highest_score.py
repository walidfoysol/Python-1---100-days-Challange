
user_inputs = input('Write down all scores of the class. (use ", " after every score)')

all_scores = user_inputs.split(", ")

# all_scores = list(map(int,all_scores))   # make all element of the list from str to int
# all_scores = [int(scores) for scores in all_scores] # make all element of the list from str to int

# all_scores.sort()
# print(f"Highest score is {all_scores[-1]}")

# highest = 0
# for scores in all_scores:
#     i = int(scores)
#     if i > highest:
#         highest = i


highest = max(all_scores)
highest = min(all_scores)

print(f"Highest score is {highest}")