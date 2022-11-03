'''Задача
В массиве найти позицию минимального и максимального числа.
Заменить все числа между позициями на нули.

8
3
2
4
85
2
4
5
1

3 2 4 85 0 0 0 1

Числа пока вводим в столбик, тут просто для наглядности.
Выводим в строку.'''
n = int(input())
arr = []
max = 0
min = 0
for i in range(n):
    x = int(input())
    arr.append(x)
    if arr[i] > arr[max]:
        max = i
    if arr[i] < arr[min]:
        min = i
print(arr)
if min > max:
    # tmp = max
    # max = min
    # min = tmp
    max, min = min, max

for i in range(min + 1, max):
    arr[i] = 0

print(arr)






