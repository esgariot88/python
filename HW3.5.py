#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:
#для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите длину ряда: '))

f3 = f4 = -1
print(f3, f4, end=' ')
 
for i in range(1, n):
    f3, f4 = f4, f3 + f4
    print(f4, end=' ')

for x in reversed(range(f4)):
    print(f4, end=' ')

f1 =0
f2 =1
print(f1, f2, end=' ')
 
for i in range(0, n):
    f1, f2 = f2, f1 + f2
    print(f2, end=' ')
