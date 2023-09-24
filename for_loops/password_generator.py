import random
import string

letters_count = int(input("How many letters would you like in your password? "))
numbers_count = int(input("How many numbers would you like in your password? "))
symbols_count = int(input("How many symbols would you like in your password? "))

total_length = letters_count + numbers_count + symbols_count
password = ""
for iterator in range(0, total_length + 1):
    if letters_count != 0:
        password += random.choice(string.ascii_letters)
        letters_count -= 1
    if numbers_count != 0:
        password += random.choice(string.digits)
        numbers_count -= 1
    if symbols_count != 0:
        password += random.choice(string.punctuation)
        symbols_count -= 1

print(password)