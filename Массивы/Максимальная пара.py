n = int(input())
arr = []
max = 0

# Найти максимальную сумму любых двух чисел в массиве
# 4
# 0 1 2 3
# 9 1 1 7
# 18

# Заполнение массива с клавиатуры
for i in range(n):
    arr.append(int(input()))

for i in range(n):
    # Начинает с i + 1, потому что нам не нужны повторяющиеся пары
    # и число не нужно складывать само с собой
    for j in range(i+1, n):
        if arr[i] + arr[j] > max:
            max = arr[i] + arr[j]

print(max)