# Библиотека для генерации случайных чисел
import random
# Массивы
# Массивы нумеруют свои элементы с 0
arr = []

count = int(input())

# append() - функция для добавления элемента в массив
for i in range(count):
    # randint(1, 100) - генерация случайного числа от 1 до 100
    arr.append(random.randint(1, 100))

print(arr)
# 0  1  2 3  4 5  6  7  8
# 12 55 7 12 6 32 12 44 74
# Кол-во локальных максимумов
# arr[i] обращение к элементу массива
indexes = []

for i in range(1, count - 1):
    if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
        indexes.append(i)
print(len(indexes))
print(indexes)
max = 0
for i in range(count):
    if arr[i] > arr[max]:
        max = i
print(max)