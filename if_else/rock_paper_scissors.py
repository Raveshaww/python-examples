import random

choice = int(input("What do you choose? 0 for Rock, 1 for Paper, or 2 for Scissors "))
computer_choice = random.randint(0,2)

if choice == 0 and computer_choice == 1:
    print("You lose")
elif choice == 0 and computer_choice == 2:
    print("You win")    
elif choice == 1 and computer_choice == 0:
    print("You win")
elif choice == 1 and computer_choice == 2:
    print("You lose")
elif choice == 2 and computer_choice == 0:
    print("You lose")
elif choice == 2 and computer_choice == 1:
    print("You win")
else:
    print(f"You tie.")