#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

multipliers=int(input("Введите число: "))
for i in range(2,multipliers + 1):
    if multipliers % i == 0:
        count = 1
        print(i)
        for j in range(2,(i//2 + 1)):
            if(i % j == 0):
                count = 0
                break
        if(count == 1):
           print(count) 
