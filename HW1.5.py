# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
import math
x1 = int(input("Введите X точки A: "))
y1 = int(input("Введите Y точки A: "))
x2 = int(input("Введите X точки B: "))
y2 = int(input("Введите Y точки B: "))

line1=x2-x1
line2=y2-y1

distanse= math.sqrt(float(line1*line1)+(line2*line2))

print(distanse)
