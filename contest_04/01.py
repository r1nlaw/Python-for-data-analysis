import numpy as np

numbers = input().strip()

array = np.array(numbers.split(), dtype=int)

result = np.where(array > 127, 1, 0)

lst = []

lst = " ".join(map(str, result))

print(lst)
