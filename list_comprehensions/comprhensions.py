answer = [name[0] for name in ["Elie", "Tim", "Matt"]]
print(answer)

answer2 = [number for number in [1,2,3,4,5,6] if number % 2 == 0]
print(answer2)


answer = [number for number in [1,2,3,4] if number in [1,2,3,4] and number in [3,4,5,6]]
print(answer)

# reverses name
answer2 = [name[::-1].lower() for name in ["Elie", "Tim", "Matt"]]
print(answer2)


answer = [number for number in range(1, 101) if number % 12 == 0 ]
print(answer)

answer = [letter for letter in "amazing" if letter not in "aeiou"]
print(answer)

## nested list example with LC
board = [[num for num in range(1,4)] for val in range(1,4)]
print(board)