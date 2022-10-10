#Задайте последовательность чисел. 
#Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random

first_numbers=[random.randint(1, 10) for i in range(10)]
second_numbers=[i for i in first_numbers if first_numbers.count(i)==1]
print(first_numbers)
print(second_numbers)
