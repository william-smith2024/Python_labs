def start_game():
    print("Welcome to the Dungeon Adventure!")
    print("You find yourself in a dark dungeon. Your goal is to find the hidden treasure.")
    first_choice()

def first_choice():
    print("\nYou are at a crossroads. Do you want to go left or right?")
    choice = input("Enter 'left' or 'right': ").lower()
    if choice == 'left':
        left_path()
    elif choice == 'right':
        right_path()
    else:
        print("Invalid choice. Please enter 'left' or 'right'.")
        first_choice()

def left_path():
    print("\nYou walk down the left path and encounter a sleeping dragon!")
    print("Do you want to sneak past the dragon or go back?")
    choice = input("Enter 'sneak' or 'back': ").lower()
    if choice == 'sneak':
        print("\nYou successfully sneak past the dragon and continue on to find the treasure!")
    elif choice == 'back':
        first_choice()
    else:
        print("Invalid choice. Please enter 'sneak' or 'back'.")
        left_path()

def right_path():
    print("\nYou walk down the right path and find a basketball.")
    print("Do you want to take the basketball with you or leave it?")
    choice = input("Enter 'take' or 'leave': ").lower()
    if choice == 'take':
        print("\nYou take the basketball with you.")
        basketball_scenario(True)
    elif choice == 'leave':
        print("\nYou leave the basketball and continue down the path.")
        basketball_scenario(False)
    else:
        print("Invalid choice. Please enter 'take' or 'leave'.")
        right_path()

def basketball_scenario(has_basketball):
    print("\nYou encounter an angry rabbit!")
    if has_basketball:
        print("Do you want to throw the basketball at the rabbit or run away?")
        choice = input("Enter 'throw' or 'run': ").lower()
        if choice == 'throw':
            print("\nYou throw the basketball at the rabbit, and it runs away. You continue your journey and find the treasure! You win!")
        elif choice == 'run':
            print("\nYou run away from the rabbit but get lost in the woods. Game over.")
    else:
        print("Do you want to run away from the rabbit?")
        choice = input("Enter 'run': ").lower()
        if choice == 'run':
            print("\nYou run away from the rabbit but get lost in the woods. Game over.")
        else:
            print("Invalid choice. Please enter 'run'.")
            basketball_scenario(False)
    play_again()

def play_again():
    choice = input("Do you want to play again? (yes/no): ").lower()
    if choice == 'yes':
        start_game()
    elif choice == 'no':
        print("Thanks for playing! Goodbye.")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
        play_again()

# Start the game
start_game()