#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
#За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
#Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

import random

candies=2021
lot=random.randrange(1,3,1)
first_player="Игрок № 1"
second_player="Игрок № 2"
sum_candies_first_player=0
sum_candies_second_player=0

if lot==1:
    current_gamer=first_player
else:
    current_gamer=second_player

while candies>0:
    print('количество оставшихся конфет: {}'.format(candies))
    while True:
        number_to_delete = int(input('ход игрока {} (1 - 28): '.format(current_gamer)))
        if number_to_delete >= 1 and number_to_delete <= 28:
            break
    if current_gamer==first_player:
        sum_candies_first_player+=number_to_delete
    elif current_gamer==second_player:
        sum_candies_second_player+=number_to_delete

    candies -= number_to_delete
    current_gamer = second_player if current_gamer == first_player else first_player


print('Конфет взял Игрок № 1 {}'.format(sum_candies_first_player))
print('Конфет взял Игрок № 2 {}'.format(sum_candies_second_player))
print('Победил {}'.format(current_gamer))  
