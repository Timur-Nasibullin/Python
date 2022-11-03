f = open('input.txt')
lines = f.readlines()
for i in range(len(lines)):
    if i % 5 == 0:
        print()
    print(f'{int(lines[i]):<4d}', end = '')