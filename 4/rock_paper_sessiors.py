import rps_game


user_score = 0
computer_score = 0

while user_score < 3 and computer_score < 3:
    result = rps_game.the_game()
        
    if result == 1:
        user_score += 1
    elif result == -1:
        computer_score += 1
        
    print(f"Score -> You: {user_score} | Computer: {computer_score}")
    print("-" * 40)  # Separator for clarity

# Final result
if user_score == 3:
    print("🎉 Congratulations! You won the game! 🎉")
else:
    print("😞 The computer won the game. Better luck next time! 😞")

