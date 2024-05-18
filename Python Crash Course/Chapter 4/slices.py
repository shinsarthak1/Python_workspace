animals = ["spider monkey", "lemur", "giraffe","Tiger","lion","octopus","elephant"]

# Print each animal.
for animal in animals:
    print(animal)

print("\n")

# Print a statement about each animal.
for animal in animals:
    print(f"A {animal} has a long tail.")

print("\nAll of these animals have long tails.")
print("The first three items in this list are:\n",animals[:3])
print("The middle three items in this list are:\n",animals[2:5])
print("The last three items in this list are:\n",animals[-1:-4:-1])