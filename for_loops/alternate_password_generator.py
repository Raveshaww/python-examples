import random
import string

letters_count = int(input("How many letters would you like in your password? "))
numbers_count = int(input("How many numbers would you like in your password? "))
symbols_count = int(input("How many symbols would you like in your password? "))

password = []

for iterator in range(0, letters_count + 1):
    password.append(random.choice(string.ascii_letters))
for iterator in range(0, numbers_count + 1):
    password.append(random.choice(string.digits))
for iterator in range(0, symbols_count + 1):
    password.append(random.choice(string.punctuation))

random.shuffle(password)

print(''.join(password))