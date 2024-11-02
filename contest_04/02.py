import numpy as np

# Чтение первой строки с параметрами
n, m, target = map(int, input().strip().split())

# Создание пустой матрицы
matrix = []

# Чтение n строк матрицы
for _ in range(n):
    row = list(map(int, input().strip().split()))
    matrix.append(row)

# Преобразование списка списков в массив numpy
arr = np.array(matrix)

# Применение условия: четные числа заменяем на target
result = np.where(arr % 2 == 0, target, arr)

# Вывод результата
for row in result:
    print(' '.join(map(str, row)))