def find_unique_registrations(n, registered_users, k, registration_requests):
    # Преобразуем списки в множества для удобства работы
    registered_set = set(registered_users)
    requests_set = set(registration_requests)
    
    # Находим уникальные заявки, которые не совпадают с уже зарегистрированными пользователями
    unique_requests = requests_set - registered_set
    
    # Сортируем уникальные заявки в лексикографическом порядке
    sorted_unique_requests = sorted(unique_requests)
    
    # Возвращаем результат в виде строки с разделителем пробел
    return ' '.join(sorted_unique_requests)

# Ввод данных пользователем
n = int(input())
registered_users = input().split()
k = int(input())
registration_requests = input().split()

# Обработка данных и вывод результата
result = find_unique_registrations(n, registered_users, k, registration_requests)
print(result)