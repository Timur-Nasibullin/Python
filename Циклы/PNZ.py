poz = 0
neg = 0
z = 0
n = int(input())
for i in range(n):
    x = int(input())
    if x > 0:
        poz += 1
    if x < 0:
        neg += 1
    if x == 0:
        z += 1
print(f'Положительных: {poz}')
print(f'Отрицательных: {neg}')
print(f'Нулей: {z}')
