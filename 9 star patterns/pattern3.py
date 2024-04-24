# Outer loop to iterate from 5 to 1 in reverse order
for i in range(5, 0, -1):
    # Inner loop to print leading spaces
    for j in range(0, 5 - i):
        print(" ", end="")
    # Inner loop to print asterisks
    for j in range(0, i):
        print("*", end="")
    # Move to the next line after printing all spaces and asterisks for each row
    print()
