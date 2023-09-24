try:
    foobar
except NameError as error:
    print(error)
except KeyError as error:
    print("Hai")
except (ZeroDivisionError, TypeError) as error:
    print(error)

print("Working anyways!")


while True:
    try: 
        num = int(input("Please enter a number: "))
    except:
        print("That's not a number")
    else:
        print("I'm in the else statement")
        break
    finally:
        print("In the finally, runs no matter what")

def divide(num1, num2):
    try:
        return num1 / num2
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"

divide(2, 1)
divide( [], "1")
divide(1,0)