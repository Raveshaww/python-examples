print("Your mission is to find the treasure.") 

game_over = False
direction = input("Would you like to go left or right? ")

if direction.lower() == "left":
    print("You arrive at a river crossing.")
    swimming = input("Would you like to swim or wait? ") 
    if swimming == "wait":
        print("Several doors appear!")
        door = input("Which door would you like to open? Blue, Red, or Yellow? ")
        if door == "red":
            print("RIP, you were burnt to death.")
        elif door == "yellow":
            print("You win!")
        elif door == "blue":
            print("RIP, eaten alive by birbs")
        else: 
            print("You were never heard from again")
    else:
        print("You were attacked by a trout, RIP.")
else: 
    print("You fell into a hole, RIP.")
