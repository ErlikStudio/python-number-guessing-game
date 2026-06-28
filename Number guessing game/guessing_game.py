import random

print("Welcome to the Number Guessing Game!")

play_again = "yes"

while play_again == "yes":

    number_to_guess = random.randint(1, 100)
    attempts = 10

    print("\nI'm thinking of a number between 1 and 100.")
    print("You have 10 attempts to guess it.")

    while attempts > 0:
        guessed_number = int(input("Enter your guess: "))

        if guessed_number == number_to_guess:
            print("You won! The number was", number_to_guess)
            break

        difference = abs(number_to_guess - guessed_number)

        if difference <= 5:
            print("🔥 You're very close!")

        elif guessed_number < number_to_guess:
            print("Too Low!")

        else:
            print("Too High!")

        attempts -= 1
        print("Attempts left:", attempts)

    if attempts == 0:
        print("Game Over! The number was", number_to_guess)

    play_again = input("Play again? (yes/no): ").lower()