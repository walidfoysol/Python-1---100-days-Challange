import random
import art
from game_data import data
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')



def compare(a,data,score):
    clear_terminal()
    print(art.logo)
    print(f"Current Score: {score}")
    print(f"Compare A: {a['name']} , a {a['description']}, from {a['country']}.")
    print(art.vs)
    data = [item for item in data if item['name'] != a['name']]
    if not data:
        clear_terminal()
        print(f"Game Over! Final Score : {score}")
        return 0
    b = random.choice(data)
    print(f"Compare B: {b['name']} , a {b['description']}, from {b['country']}.")
    choice = input(f"Who has more followers? type 'A' or 'B': ").upper()
    if choice == 'A' and a['follower_count'] > b['follower_count']:
        score += 1
        compare(b,data,score)
    elif choice == 'B' and b['follower_count'] > a['follower_count']:
        score += 1
        compare(b,data,score)
    else:
        clear_terminal()
        print(f"Game Over! Final Score : {score}")


score = 0
a = select_random(data)
compare(a, data, score)