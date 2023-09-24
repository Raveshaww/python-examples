import random

def guessing_game():
    computer_wins = True
    while computer_wins:
        random_number = random.randint(0,100)
        guessed_number = int(input("Pick a number between 1 and 100\n"))
        if random_number == guessed_number:
            print('You guessed right!')
            computer_wins = False
        elif guessed_number < random_number:
            print("Too low")
        elif guessed_number > random_number:
            print("Too high")
        print(f"You guessed {guessed_number}, while the computer chose {random_number}")

guessing_game()