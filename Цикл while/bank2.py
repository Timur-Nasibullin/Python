# Банковский депозит

startSum = int(input())
percent = int(input())
targetSum = int(input())
x = 0
monthCount = 0
while startSum < targetSum:
    x = startSum * percent / 100
    startSum += x
    monthCount = monthCount + 1
    # :.2f - ограничение дробной части до 2ух знаков
    print(f'{monthCount} - {startSum:.2f}')