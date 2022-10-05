#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
#между максимальным и минимальным значением дробной части элементов.
#Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19


new_list = [1.1, 1.2, 3.1, 5, 10.01]  
new_list2=[]
value=0
for i in range (len(new_list)):
    value=new_list[i]%1
    new_list2.append(round(value,3))
new_list2=[i for i in new_list2 if i != 0]
result=(max(new_list2))-(min(new_list2))    
print(result)  
