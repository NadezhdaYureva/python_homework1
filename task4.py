# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

a = int(input("Введите номер четверти "))

if a == 1:
    print('Диапазон возможных координат - x > 0 и y > 0')
if a == 2:
    print('Диапазон возможных координат - x < 0 и y > 0')
if a == 3:
    print('Диапазон возможных координат - x < 0 и y < 0')
if a == 4:
    print('Диапазон возможных координат - x > 0 и y < 0')