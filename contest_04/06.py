import math

# Чтение входных данных
k, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(k)]

# Вычисляем IDF для каждого столбца
idf_values = []
N = k  # Общее количество текстов (строк)

for j in range(m):
    # Подсчитываем, в скольких текстах присутствует слово в столбце j
    nt = sum(1 for i in range(k) if matrix[i][j] > 0)
    
    # Вычисляем IDF по формуле
    idf = math.log(N / (nt + 1)) + 1
    
    # Округляем до двух знаков после запятой
    idf_values.append(round(idf, 2))

# Выводим результат
print(' '.join(map(str, idf_values)))
