import numpy as np

# Чтение входных данных
input_data = input().strip()
vector = np.array(list(map(int, input_data.split())))

# Определение индексов элементов, которые лежат в диапазоне от -100 до 100 включительно
indices = np.where((vector >= -100) & (vector <= 100))[0]

# Вывод результата
print(" ".join(map(str, indices)))