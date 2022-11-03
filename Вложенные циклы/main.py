for i in range(1, 10):
    for j in range(1, 10):
        if i == j or i + j == 10:
            print(f'{0:<3d}', end=' ')
        else:
            print(f'{i * j:<3d}', end=' ')
    print()