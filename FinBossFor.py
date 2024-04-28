N = int(input('Введите число: '))
count = 0
for i in range(N):
    if i == 0:
        count = 0
    else:
        count = count + 1 / i
print('Выражение 1 + 1 / N равно: ', count)
