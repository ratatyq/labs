# ввод размеров
while True:
    try:
        # защита от дурака
        n = int(input("Строки: "))
        m = int(input("Столбцы: "))
        if n > 0 and m > 0:
            break
    except:
        pass
    print("Неверный ввод")

# ввод матрицы
a = []
for i in range(n):
    row = []
    while len(row) < m:
        # если ввод правильный, в список добавляется число
        try:
            x = int(input(f"[{i+1},{len(row)+1}]: "))
            row.append(x)
        except:
            print("Введите число")
    a.append(row)

# обработка
for i in range(n):
    s = 0
    for j in range(m-1):
        s += a[i][j]
    a[i][m-1] = s

# вывод
print("Результат:")
for x in a:
    for y in x:
        print(y, end=" ")
    print()