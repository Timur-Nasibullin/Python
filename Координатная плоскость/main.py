x = int(input())
y = int(input())

# Условная конструкция
# if...else...elif
# > < >= <= != ==
# or and

# Задача
# На вход подаются координаты точки
# Необходимо вывести четверть в которой находится точка
# или сообщить, что точка лежит на оси
'''
if x > 0:
    if y > 0:
        print('I')
    if y < 0:
        print('IV')
if x < 0:
    if y < 0:
        print('III')
    if y > 0:
        print('II')
'''
if x > 0 and y > 0:
    print('I')
if x > 0 and y < 0:
    print('IV')
if x < 0 and y < 0:
    print('III')
if x < 0 and y > 0:
    print('II')
if x == 0 or y == 0:
    print('На оси')
