import random


names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
persons = len(names)

selected_person = random.randint(0,persons-1)

print(f"{names[selected_person]} will pay the bill!")