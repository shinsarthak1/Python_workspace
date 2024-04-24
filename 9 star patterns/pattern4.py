# Outer loop to iterate from 1 to 5
for i in range(1, 6):
    # Inner loop to print leading spaces
    for k in range(1, 6 - i):
        print(" ", end="")
    # Inner loop to print asterisks
    for j in range(1, i + 1):
        print("* ", end="")
    # Move to the next line after printing spaces and asterisks for each row
    print("")
