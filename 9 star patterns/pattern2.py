# Inverted half pyramid

# Outer loop to iterate from 5 to 1 in reverse order
for i in range(5, 0, -1):
    # Inner loop to print asterisks
    for j in range(1, i + 1, 1):
        print("*", end="")
    # Move to the next line after printing asterisks for each row
    print("")

