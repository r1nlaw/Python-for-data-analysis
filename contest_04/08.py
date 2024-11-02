import numpy as np

# Чтение входных данных
input_data = input().strip()
vector = np.array(list(map(float, input_data.split())))

# Возведение каждого элемента в квадрат
vector_squared = vector ** 2

# Вычисление синуса от каждого элемента
vector_sin = np.sin(vector_squared)

# Определение минимального элемента
min_element = np.min(vector_sin)

# Вывод результата, округленного до двух знаков после запятой
print(f"{min_element:.2f}")