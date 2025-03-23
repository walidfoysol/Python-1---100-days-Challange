import random
import art


def count_value(lst,dict):
    value = 0
    for element in lst:
        if element == 'A' and (value + dict[element]) > 21:
            value += 1
        else:
            value += dict[element]
    return value

def declare(n1,n2):
    print(f"Your value: {n1}")
    print(f"Computer value: {n2}")
    if n1 > n2 and n1 < 22 or n1<22 and n2 > 21:
        print("You won!")
    else:
        print("Computer won!")


def game():
    cards = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
    user_cards = random.sample(list(cards.keys()),2)
    bot_cards = random.sample(list(cards.keys()),2)
    print(f"Your cards : [{user_cards[0]}, {user_cards[1]}]")
    print(f"Computer's first card: {bot_cards[0]}")
    user_value = count_value(user_cards,cards)
    bot_value = count_value(bot_cards,cards)
    check = input(f"Type 'y' to get another card, Type 'n' to pass: ").lower()
    while check == 'y':
        user_cards += random.sample(list(cards.keys()),1)
        bot_cards += random.sample(list(cards.keys()),1)
        print(f"Your cards are: {", ".join(user_cards)}")
        print(f"Computer's cards are: {", ".join(bot_cards)}")
        user_value = count_value(user_cards, cards)
        bot_value = count_value(bot_cards, cards)
        check = input(f"Type 'y' to get another card, Type 'n' to pass: ").lower()
    declare(user_value,bot_value)
    main()
        


def main():
    consent = str(input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ")).lower()
    if consent == 'y':
        print(f"{art.logo}")
        game()

main()