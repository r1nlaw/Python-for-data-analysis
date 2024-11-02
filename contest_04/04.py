import numpy as np

# Чтение входных данных
k, m = map(int, input().split())
matrix1 = np.array([list(map(float, input().split())) for _ in range(k)])
matrix2 = np.array([list(map(float, input().split())) for _ in range(k)])

# Вычисление среднеквадратичного отклонения
msd = np.mean((matrix1 - matrix2) ** 2)

# Округление до 2 знаков после запятой
msd_rounded = round(msd, 2)

# Вывод результата
print(msd_rounded)