import random

def get_winner(player, computer):
    wins = {
        "rock": ["scissors"],
        "paper": ["rock"],
        "scissors": ["paper"]
    }
    wins_extended = {
        **wins,
        "lizard": ["spock", "paper"],
        "spock": ["scissors", "rock"]
    }

    if player == computer:
        return "tie"
    elif computer in wins_extended.get(player, []):
        return "player"
    else:
        return "computer"


def play_game():
    print("Welcome to Rock Paper Scissors!")
    variant = input("Choose your game (classic or extended): ").lower().strip()

    # Set choices based on variant
    classic_choices = ["rock", "paper", "scissors"]
    extended_choices = classic_choices + ["lizard", "spock"]

    if variant == "extended":
        choices = extended_choices
    else:
        choices = classic_choices

    print(f"You selected {variant} mode. Choices are: {', '.join(choices)}")

    # Ask rounds & initialize scores
    rounds = int(input("How many rounds do you want to play? "))
    player_score = 0
    computer_score = 0

    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}!")

        # Computer's choice
        computer_choice = random.choice(choices)
        print("Computer has made its choice!")

        # Player's choice
        player_choice = input(f"Choose your move ({', '.join(choices)}): ").lower().strip()
        if player_choice not in choices:
            print("Invalid choice! This round is skipped.")
            continue

        print(f"You chose {player_choice}, computer chose {computer_choice}.")

        # Determine winner
        winner = get_winner(player_choice, computer_choice)
        if winner == "tie":
            print("It's a tie!")
        elif winner == "player":
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        # Show current score
        print(f"Score: You {player_score} - Computer {computer_score}")

    # Final result
    print("\nGame Over!")
    if player_score > computer_score:
        print("🎉 Congratulations! You won the game!")
    elif computer_score > player_score:
        print("💻 Computer won the game, Better luck next time!")
    else:
        print("🤝 It's a Tie, Well Played!")


if __name__ == "__main__":
    play_game()
