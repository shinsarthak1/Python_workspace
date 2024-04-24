for i in range(1, 6):
    k = 65  # ASCII value for 'A'
    for j in range(1, 7 - i):
        print(" ", end="")
    for l in range(1, i + 1):
        print(chr(k), end=" ")
        k += 1  # Move to the next character
    print("")
