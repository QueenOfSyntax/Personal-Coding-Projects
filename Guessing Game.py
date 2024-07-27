import random

def guessing_game():
    secretNumber = random.randint(1, 100)
    attempts = 0

    while attempts < 10:
        user_guess = int(input("Guess the number between 1 and 100: "))
        attempts += 1
        if user_guess < secretNumber:
            print("Too low! Try a higher number.")
        elif user_guess > secretNumber:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You've guessed the number {secretNumber} correctly in {attempts} attempts!")
            return

    print(f"Sorry, you've run out of guesses! The correct number was {secretNumber}.")

guessing_game()
