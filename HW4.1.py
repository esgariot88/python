#Вычислить число c заданной точностью d
#Пример:
#- при d = 0.001, π = 3.141    

import random

d= float(input("Введите точность вещественного числа: "))
number=float(random.uniform(5,10))
n=str(d).replace('.', '')
count=n.count('0')
truenumber=round(number,count)
print(truenumber)
