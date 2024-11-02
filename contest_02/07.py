def calculate_water(n, heights):
    left_max = [0] * n
    right_max = [0] * n
    
    # Заполняем массив максимальных высот слева
    left_max[0] = heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], heights[i])
    
    # Заполняем массив максимальных высот справа
    right_max[n - 1] = heights[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i])
    
    # Вычисляем количество воды на каждом столбце
    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - heights[i]
    
    return water

def main():
    n = int(input())
    heights = list(map(int, input().split()))
    result = calculate_water(n, heights)
    print(result)

if __name__ == "__main__":
    main()