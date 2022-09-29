# Задайте число N и создайте список, заполненный числами из промежутка [-N, N]. 
#Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

n= int(input("Введите число: "))
numbers = []
data = open('file.txt', 'r')
ind= data.readlines()
ind_string = '' 
for line in ind:
    ind_string += line.strip()
print(ind_string)

for i in range (-n,n):

    new_arg=i+1

    numbers.append(new_arg)

    work=numbers[ind_string[0]]*numbers[ind_string[1]]*numbers[ind_string[2]]

    print(numbers)

    print(work)

data.close()
