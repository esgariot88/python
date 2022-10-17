# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# new_list = [2, 3, 5, 9, 3]
# summ=0

# for i in range(len(new_list)):
#     if i%2 == 1:
#         summ+= new_list[i]
        
# print(summ)

#Оптимизированно
new_list = [2, 3, 5, 9, 3]
sum_elements=sum([new_list[i] for i in range(len(new_list)) if i%2 == 1])
print(sum_elements)
