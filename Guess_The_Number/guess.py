from random import randint


def guess_the_number():
    print("Guess the number between 1 and 100\n")
    number = randint(1, 100)
    guess = 0
    num_of_guesses = 0
    while guess != number:
        num_of_guesses += 1
        guess = int(input("What's your guess? "))
        if guess > number:
            print("Too high! Guess lower.")
        if guess < number:
            print("Too low! Guess higher.")
        if guess == number:
            print(f"Correct! Nicely done. You did this in {num_of_guesses} tries.")


guess_the_number()
