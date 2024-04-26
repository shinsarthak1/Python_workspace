num = int(input("Enter a number: ")) # 151
original_num = num
rev = 0
while num > 0: # is 151 > 0 yes. is 15>0 yes is 1>0 yes
    digit = num % 10 #1 151 % 10 = 1 #2 15 % 10 = 5 #3 1%10 = 1
    rev = rev * 10 + digit   #1 0*10 + 1 = 1 #2 1*10 +5 = 15 #3 15*10+1 = 151
    num //= 10 # 151 //10 -> 15, 15//10
if original_num == rev:
    print(f"The given number is a palindrome number.")
else:
    print("The given number is not a palindrome number.")
    # Hence, 151 is a palindrome number.3
