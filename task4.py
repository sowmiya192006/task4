import random

print("Welcome to Rock, Paper, Scissors!")

choices = ["rock", "paper", "scissors"]
user_score = 0
comp_score = 0

def determine_winner(user, comp):
    if user == comp:
        return "tie"
    elif (user == "rock" and comp == "scissors") or \
         (user == "scissors" and comp == "paper") or \
         (user == "paper" and comp == "rock"):
        return "user"
    else:
        return "comp"

while True:
    user_choice = input("\nChoose rock, paper, or scissors: ").lower()
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    comp_choice = random.choice(choices)
    print(f"Computer chose: {comp_choice}")

    winner = determine_winner(user_choice, comp_choice)
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        comp_score += 1

    print(f"Scores -> You: {user_score} | Computer: {comp_score}")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Final Scores:")
        print(f"You: {user_score} | Computer: {comp_score}")
        break
