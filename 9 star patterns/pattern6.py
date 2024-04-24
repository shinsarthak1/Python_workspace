# Outer loop to iterate over rows from 1 to 5
for i in range(1, 6):
    # Inner loop to print leading spaces
    for j in range(1, i):
        print(" ", end="")
    # Inner loop to print asterisks
    for k in range(1, 7 - i):
        print("* ", end="")
    # Move to the next line after printing each row
    print(" ")
