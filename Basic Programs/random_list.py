import random


list1 = []


for num in range(10):
    list1.append(random.randint(1,100))
print(list1)


odd_list = []
even_list = []


for number in list1:
    if number % 2 == 0:
        even_list.append(number)
    else:
        odd_list.append(number)


print("odd numbers: ", odd_list)
print("even numbers: ",even_list)


