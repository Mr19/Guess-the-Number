import random


def main():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.\n")
    difficulty = input("Choose a difficulty. Type 'easy or 'hard': ").lower()

    difficulty_dict = {"easy": 10, "hard": 5}
    computer_guess = random.randint(1, 100)

    attempts = difficulty_dict[difficulty]

    while attempts:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a Guess: "))
        if guess == computer_guess:
            print(f"You Got it!, the answer was {computer_guess}")
            attempts = 0
        elif guess > computer_guess:
            if attempts == 1:
                print("Too High")
                attempts -= 1
            else:
                print("Too High\nGuess Again.")
                attempts -= 1
        else:
            if attempts == 1:
                print("Too Low")
                attempts -= 1
            else:
                print("Too Low\nGuess Again.")
                attempts -= 1
        if attempts == 0 and guess != computer_guess:
            print("You've run out of guesses, you lose")


if __name__ == '__main__':
    main()

