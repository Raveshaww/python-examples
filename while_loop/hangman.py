import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = list("_" * len(chosen_word))           
losses = 0
game_won = False

while not game_won and losses < 7:
    letter_in_word = False
    iterator = 0
    chosen_letter = input("Please pick a letter: ").lower()
    for letter in chosen_word:
        if chosen_letter == letter:
            display[iterator] = chosen_letter
            letter_in_word = True
        iterator += 1
    
    if not letter_in_word:
        print(f"{chosen_letter} is not in the word!")
        print(f"You have lost {losses + 1} times!")
        losses += 1
    
    print("".join(display))

    if ("".join(display)) == chosen_word:
        print("You win!")
        game_won = True

    print()

