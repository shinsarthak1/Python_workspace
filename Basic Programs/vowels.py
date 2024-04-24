list1 = [x.lower() for x in ["Apple","Mango","Chickoo"]] # initializing list
print(list1)
vowels = "aeiou" # string
count = 0
for word in list1: # Iterate through each string in the list
    for char in word:  # Iterate through each character in the string
        if char in vowels:  # Check if the character is a vowel
            count = count + 1
print(f"The number of vowels in the given list is {count}.")




