import numpy as np

# Чтение входных данных
n, m = map(int, input().split())
image = np.array([list(map(int, input().split())) for _ in range(n)])

# Определение фильтра
kernel = np.array([
    [-1, -1, -1],
    [-1,  9, -1],
    [-1, -1, -1]
])

# Выполнение свёртки
output = np.zeros((n-2, m-2), dtype=int)
for i in range(1, n-1):
    for j in range(1, m-1):
        output[i-1, j-1] = np.sum(image[i-1:i+2, j-1:j+2] * kernel)

# Ограничение значений в диапазоне [0, 255]
output = np.clip(output, 0, 255)

# Вывод результата
for row in output:
    print(' '.join(map(str, row)))