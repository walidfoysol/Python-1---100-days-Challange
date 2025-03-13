map = [["🎁","🎁","🎁"],["🎁","🎁","🎁"],["🎁","🎁","🎁"]]


print(f"{map[0]}\n{map[1]}\n{map[2]}\n")

location = input("Where do you want to hide the tresure? ")

map[int(location[1])-1][int(location[0])-1] = "💰"

print(f"{map[0]}\n{map[1]}\n{map[2]}\n")

