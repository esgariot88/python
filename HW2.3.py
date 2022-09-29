#Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.
#Пример:
#Для n = 5: сумма = 11,55

n= int(input("Введите число: "))
numbers = []
summ=0
for i in range (n):
    new_arg=(1+ (1/n))**n
    numbers.append(new_arg)
    summ+=numbers[i]
    print(numbers)
    print(summ)
