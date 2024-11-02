import matplotlib.pyplot as plt
import numpy as np

# Пример данных
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Создание графика
plt.figure(figsize=(10, 5))
plt.plot(x, y, color='blue', label='sin(x)', linewidth=2)

# Заголовок и метки

plt.xlabel('Ось X')
plt.ylabel('Ось Y')

# Легенда
plt.legend()

# Сетка
plt.grid(True, linestyle='--', color='gray')

# Установка пределов по осям
plt.xlim(0, 10)
plt.ylim(-1.5, 1.5)

# Подписи на осях
plt.xticks(np.arange(0, 11, 1))
plt.yticks(np.arange(-1, 2, 0.5))

# Показать график
plt.show()

print('1')
