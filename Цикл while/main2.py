x = -1
count = -1
sum = 0
# Чтение множества чисел до тех пор, пока пользователь не введёт 0
# Найти среднее арифметическое
while x != 0:
    x = int(input())
    count = count + 1
    sum = sum + x
print(f'{sum / count}')