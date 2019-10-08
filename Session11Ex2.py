#Determine the average of 4 random numbers

def avg (list_numbers):
    sum = 0
    for i in list_numbers:
        sum = sum+i

    average = sum/len(list_numbers)
    return average

number_list = []
import random
for i in range(4):
    number_list.append(random.randint(-1000, 1000))
a = avg (list_numbers = number_list)
print(a)