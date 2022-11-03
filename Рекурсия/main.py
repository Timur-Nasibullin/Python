# Вывести ряд чисел от 1 до n

def printSeq(n):
    if n > 0:
        printSeq(n - 1)
        print(n, end=' ')

def sumSeq(n):
    if n > 0:
        return sumSeq(n - 1) + n
    return 0

printSeq(10)
print()
print(sumSeq(10))