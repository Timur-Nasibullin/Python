a = int(input())
b = int(input())
for i in range(a, b):
    x = 0
    d1 = 0
    d2 = 0
    d3 = 0
    d4 = i
    for j in range(1, i+1):
        if i % j == 0:
            x += 1
            if d1 == 0:
                d1 = j
            elif d2 == 0:
                d2 = j
            elif d3 == 0:
                d3 = j
    if x == 4:
        print(f'{i} : {d1}, {d2}, {d3}, {d4}')

