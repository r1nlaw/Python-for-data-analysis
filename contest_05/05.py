import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Загрузка изображения
image_path = "Lenna.png"
image = Image.open(image_path)

# Уменьшение размера изображения до 128x128 пикселей
resized_image = image.resize((128, 128))

# Преобразование изображения в массив numpy
image_array = np.array(resized_image)

# Отображение изображения с помощью imshow
plt.imshow(image_array)
plt.axis('off')  # Отключение осей
plt.show()

# Вывод для проверки
print('1')