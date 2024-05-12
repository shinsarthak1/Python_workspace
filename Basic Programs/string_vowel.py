'''

Write a program that accepts a string from the user and display the same string

after removing vowels from it.

'''


inputted_string = "Hello! My name is Sarthak Shinde. I love to read books and play guitar."

vowels = ['a','e','i','o','u','A','E','I','O','U']

filtered_string = ''
for char in inputted_string:
    if char not in vowels:
        filtered_string += char
print("The string after removing vowels is ",filtered_string)
