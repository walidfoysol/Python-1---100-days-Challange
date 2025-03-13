import random

def the_game():
    game = ["rock", "paper", "scissors"]

    user_choose = input("Choose an option by writing rock or paper or scissors \n =").lower()
    computer_choose = random.choice(game)

    # Display user choice with ASCII art
    print(f"You chose {user_choose}")
    if user_choose == "rock":
        print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
    elif user_choose == "paper":
        print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
    elif user_choose == "scissors":
        print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
    else:
        print("Invalid input! Please enter rock, paper, or scissors.")
        return the_game()  # Restart the game if input is invalid

    # Display computer choice with ASCII art
    print(f"Computer chose {computer_choose}")
    if computer_choose == "rock":
        print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
    elif computer_choose == "paper":
        print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
    elif computer_choose == "scissors":
        print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

    # Determine the winner
    if user_choose == computer_choose:
        print("It is a draw!")
        return 0
    elif (user_choose == "rock" and computer_choose == "scissors") or \
         (user_choose == "paper" and computer_choose == "rock") or \
         (user_choose == "scissors" and computer_choose == "paper"):
        print("You won this round!")
        return 1
    else:
        print("Computer won this round!")
        return -1