
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

print("Specify row-column like this: 12")
position = input("Where do you want to put the X? ")

column_number, row_number  = int(list(position)[0]) - 1 , int(list(position)[1]) - 1

map[row_number][column_number] = "X"

print(f"{row1}\n{row2}\n{row3}")
