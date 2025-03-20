
import art
import os

print(art.logo)
auction_bidders = {}
auction = False
while not auction:
    name = input(f"What is your name? ")
    bid = int(input(f"What's your bid? "))
    auction_bidders[name] = bid
    consent = input("Are there any other bidders? (type 'yes' or 'no')").lower()
    if consent == "no":
        auction = True

max_key = max(auction_bidders, key = auction_bidders.get)
os.system("cls")
print(f"Highest bid is {auction_bidders[max_key]} & This auction's winner is {max_key}")




# highest = 0
# winner_name = ""
# for thing in auction_bidders:
#     if highest < auction_bidders[thing]:
#         highest = auction_bidders[thing]
#         winner_name = thing
    
# print(f"Highest bid is {highest} & This auction's winner is {winner_name}")

