"""
The Number Guessing Game is a simple command-line (CLI) Python program where:

1. The computer randomly picks a number within a given range (say, 1–100).
2. The user has to guess that number.
3. After each guess, the program gives hints like “Too high” or “Too low.”
4. The game ends when the user guesses correctly.
   And, the program displays how many attempts it took.
"""

import random


def number_guess_game():
    """Main function that runs the number guessing game."""

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    # Initialize the number of attempts
    attempts = 0

    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            input_number = int(input("\nEnter your guess: "))
            attempts += 1

            if input_number == number_to_guess:
                print(f'Correct! You guessed it in {attempts} attempts. 🎉')
                # End the round and exit
                break

            if input_number < number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

        except ValueError:
            print("Invalid input; please enter a valid number.")


def main():
    """Main function"""
    number_guess_game()
    while input("\nDo you want to play again? (yes/no): ") == "yes":
        number_guess_game()


if __name__ == "__main__":
    main()
