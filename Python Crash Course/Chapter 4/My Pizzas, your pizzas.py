pizzas = ['Cheese Pizza', 'Vegetable Pizza', 'Pasta and Momo Pizza']
# for pizza in pizzas:
#     print(f"This is {pizza},and you heckin love it!!!")

print("I really love my Pizza")

friend_pizzas = pizzas[:]
print(friend_pizzas)

pizzas.append('Pepperoni')
friend_pizzas.append('Margarita')

print("My favourite pizzas are: ")
for pizza in pizzas:
    print("- "+pizza)

print("My friend's favourite pizzas are: ")
for pizza in friend_pizzas:
    print("- "+pizza)
