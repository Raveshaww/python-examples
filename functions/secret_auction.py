import os

print("Welcome to the secret auction program.")

bidders_remaining = True
bidders = {}

def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

while bidders_remaining:

    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    additional_bidders = input("Are they any other bidders? Please type 'yes' or 'no': ")

    bidders[name] = bid

    if additional_bidders == "no":
        bidders_remaining = False

    clear()

# select highest bidder
winner = max(bidders, key=bidders.get)

print(f"{winner} wins with ${bidders[winner]}")
