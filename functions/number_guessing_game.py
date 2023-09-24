import random

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty: 'easy' or 'hard': ").lower()

computer_number = random.choice(range(1, 101))

if difficulty == "easy":
    attempts = 10
else: 
    attempts = 5

player_win = False
while attempts > 0 and player_win == False:
    guess = int(input("Please guess a number: "))

    if guess == computer_number:
        print("You win!")
        player_win = True
        break
    elif guess > computer_number:    
        print("Number too high!")
    elif guess < computer_number:
        print("Number too low")

    attempts -= 1  
    print(f"Attempts remaining: {attempts}\n")  

if player_win == False:
    print(f"The number was: {computer_number}")