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



if __name__ == "__main__":
    play_game()