from collections import Counter

def print_histogram(text):
    # Подсчитываем частоту каждого символа
    char_count = Counter(text)
    
    # Получаем список символов, отсортированный по возрастанию кода ASCII
    sorted_chars = sorted(char_count.keys())
    
    # Находим максимальное количество вхождений символа
    max_count = max(char_count.values())
    
    # Выводим гистограмму
    for i in range(max_count, 0, -1):
        line = ""
        for char in sorted_chars:
            if char_count[char] >= i:
                line += "#"
            else:
                line += " "
        print(line)
    
    # Выводим символы под гистограммой
    print("".join(sorted_chars))

def main():
    # Считываем текст
    text = input().strip()
    
    # Выводим гистограмму
    print_histogram(text)

if __name__ == "__main__":
    main()