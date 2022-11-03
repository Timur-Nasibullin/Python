# Задаётся кол-во элементов
# Далее в массив вводятся все элементы
# Сформировать два массива: в одном положительные,
# в другом отрицательные

count = int(input())
arr = []
for i in range(count):
    arr.append(int(input()))
positive = []
negative = []
sump = 0
sumn = 0
for i in range(count):
    if arr[i] > 0:
        positive.append(arr[i])
    if arr[i] < 0:
        negative.append(arr[i])
for i in range(len(negative)):
    print(negative[i], end = ' ')
    sumn += negative[i]
print(sumn)
for i in positive:
    print(i, end = ' ')
    sump += i
print(sump)


