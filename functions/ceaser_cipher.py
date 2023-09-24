import string

def caesar(text, shift, direction):
    # This is to avoid an issue with Z
    list_of_letters = list(string.ascii_lowercase) + list(string.ascii_lowercase)
    shifted_message = ""
    if direction == "decode":
        for letter in text:
            shifted_letter = list_of_letters.index(letter) - shift
            shifted_message += str(list_of_letters[shifted_letter])
        print(f"Here's the decoded result: {shifted_message}")
    elif direction == "encode": 
        for letter in text:
            shifted_letter = list_of_letters.index(letter) + shift
            shifted_message += str(list_of_letters[shifted_letter])
        print(f"Here's the encoded result: {shifted_message}")
    else:
        print("That is not a valid action.")

more_work = "yes"

while more_work == "yes":

    action = input("Do you wish to encode or decode a message?\n")
    message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text=message, shift=shift, direction=action)
    more_work = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if more_work == "no":
        break
