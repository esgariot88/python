#Напишите программу, которая найдёт произведение пар чисел списка. 
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

new_list = [2, 3, 4, 5, 6] 
new_list2 = []
work = 0

for i in range(len(new_list)):
    work= new_list[i]*new_list[-1-i]
    new_list2.append(work)
        
print(new_list2)


new_list2=list(set(new_list2))
    

print(new_list2)
