# Цикл for
# Используется, когда можно чётко посчитать кол-во повторений
# range(начало, [конец], [шаг])

# Задача
# Найти сумму чисел от а до b
a = int(input())
b = int(input())
sum = 0
for i in range(a, b + 1):
    # sum += i
    sum = sum + i

print(sum)