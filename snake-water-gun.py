import random

def get_user_choice():
    print("Enter your choice: Snake, Water, or Gun")
    user_choice = input().lower()
    while user_choice not in ['snake', 'water', 'gun']:
        print("Invalid choice. Please enter Snake, Water, or Gun.")
        user_choice = input().lower()
    return user_choice

def get_computer_choice():
    return random.choice(['snake', 'water', 'gun'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'snake' and computer_choice == 'water') or \
         (user_choice == 'water' and computer_choice == 'gun') or \
         (user_choice == 'gun' and computer_choice == 'snake'):
        return "You win!"
    else:
        return "Computer wins!"

def snake_water_gun():
    print("Welcome to Snake-Water-Gun game!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose {user_choice.capitalize()}")
        print(f"Computer chose {computer_choice.capitalize()}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        print("Do you want to play again? (yes/no)")
        play_again = input().lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    snake_water_gun()
