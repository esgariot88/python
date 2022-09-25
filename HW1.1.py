# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

dayoftheweek = int(input("Введите первое число: "))
if dayoftheweek==1:
    print("Понедельник")
elif dayoftheweek==2:
    print("Вторник")
elif dayoftheweek==3:
    print("Среда")
elif dayoftheweek==4:
    print("Четверг")
elif dayoftheweek==5:
    print("Пятница")
elif dayoftheweek==6:
    print("Суббота")
elif dayoftheweek==7:
    print("Воскресенье")
if dayoftheweek < 6: 
    print("Будний день")
else:
    print("Выходной")
