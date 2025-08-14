def play_game():
    print("Welcome to Rock Paper Scissor!")
    variant = input("Choose your game (classis or extended): ").lower().strip()
    print(f"You selected the {variant} version. Let's Start!")

if __name__ == "__main__":
    play_game()