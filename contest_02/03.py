def print_multiplication_table(row, col):
    # Формируем заголовок таблицы
    header = "    |"
    for j in range(1, col + 1):
        header += f"{j:4}"
    print(header)
    
    # Формируем разделительную линию
    separator = "   " + "-" * (4 * col + 2)
    print(separator)
    
    # Формируем строки таблицы
    for i in range(1, row + 1):
        line = f"{i:4}|"
        for j in range(1, col + 1):
            line += f"{i * j:4}"
        print(line)

# Ввод данных пользователем
row, col = map(int, input().split())

# Вывод таблицы умножения
print_multiplication_table(row, col)