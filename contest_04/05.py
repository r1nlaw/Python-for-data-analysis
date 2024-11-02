import numpy as np

# Чтение входных данных
k, m = map(int, input().split())
matrix = np.array([list(map(float, input().split())) for _ in range(k)])

# Нормирование каждой строки на её длину
normalized_matrix = matrix / np.linalg.norm(matrix, axis=1, keepdims=True)

# Округление до второго знака после запятой
normalized_matrix = np.round(normalized_matrix, 2)

# Вывод результата
for row in normalized_matrix:
    print(' '.join(map(str, row)))