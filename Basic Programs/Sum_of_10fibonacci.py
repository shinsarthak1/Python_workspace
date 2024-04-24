# Fibonacci series - 0 1 1 2 3 5 8 13 21 34 55 89

# Taking user input
num = int(input("Enter a number: "))

# Checking if the input is at least 10, if not, set it to 10
if num < 10:
    num = 10

# Initializing the first two Fibonacci numbers
fb_n1 = 0
fb_n2 = 1

sum = 0

# Generating fibonacci series upto nth
for i in range(2, num+1):
    next_fb_n = fb_n1 + fb_n2
    fb_n2 = fb_n1
    fb_n1 = next_fb_n
# Calculating sum of first 10 fibonacci nums

    if i < num + 1:
        sum = sum + next_fb_n

print(sum)
