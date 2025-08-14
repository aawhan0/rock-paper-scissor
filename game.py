import random

def get_winner(player, computer):
    wins={
        "rock": ["scissors"],
        "paper": ["rock"],
        "scissors": ["paper"]
    }


    wins_extended= {
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
    print("Welcome to Rock Paper Scissor!")
    variant = input("Choose your game (classis or extended): ").lower().strip()

    #Set choice based on variant:
    classic_choices = ["rock", "paper", "scissors"]
    extended_choices = classic_choices + ["lizard", "spock"]

    if variant == "extended":
        choices = extended_choices
    else:
        choices = classic_choices

    print(f"You selected {variant} mode. Choices are: {', '.join(choices)}")

    # Computer makes a choice randomly from the list
    computer_choice = random.choice(choices)
    print(f"Computer has made its choice!")

    player_choice = input(f"Choose your move ({', '.join(choices)}):").lower().strip()
    if player_choice not in choices:
        print("Invalid choice! Please choose from the list.")
        return

    print(f"You chose {player_choice}, computer chose {computer_choice}.")
    winner = get_winner(player_choice, computer_choice)
    if winner == "tie":
        print("You win this round!")
    else:
        print("Computer wins this round!")    


if __name__ == "__main__":
    play_game()