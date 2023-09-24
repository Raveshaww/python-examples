def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    return number1 / number2

# We are assigning the above functions as the values in this dict
# Defining it this way, without the (), means the function isn't being called here
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print("Welcome to the calculator app.")
new_calc = True

while new_calc:
    number1 = float(input("Enter the first number: "))
    operator = input("+, -, *, or /: ")
    number2 = float(input("Enter the second number: "))
    calculation_function = operations[operator]

    # Basically, we're dynamically grabbing the function to run rather than a long if statement section
    answer = calculation_function(number1, number2)

    print(f"{number1} {operator} {number2} = {answer}")

    new_calc_check = input("Would you like to continue the current result? y / n: ")
    if new_calc_check.lower() == "y":
        while True: 
            operator = input("+, -, *, or /: ")
            number2 = float(input("Enter the second number: "))
            calculation_function = operations[operator]
            answer2 = calculation_function(answer, number2)
            print(f"{answer} {operator} {number2} = {answer2}")
            new_calc_check = input("Would you like to continue the current result? y / n: ")
            if new_calc_check.lower() == "n":
                break