bill = float(input("What was the bill? "))
people = int(input("How many people are paying? "))
tip = int(input("What percentage tip would you like to give? "))

personal_total = round(bill / people * (tip / 100 + 1), 2)
print(f"You each need to pay {personal_total}")