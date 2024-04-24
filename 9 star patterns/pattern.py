# Half pyramid

# Loop through a range from 1 to 6 (not including 6)
for i in range(1, 6):
    # Nested loop that runs 'i' times for each iteration of the outer loop
    for j in range(1, i + 1):
        # Print an asterisk without a newline at the end
        print("*", end="")
    # After the inner loop finishes, print a newline to move to the next row
    print("")
