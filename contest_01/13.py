num1, num2 = list(map(int, input().split()))

count_for_nechet = 0

for i in range(num1, num2 + 1, 1):
    if i % 2 == 1:
        count_for_nechet += 1
print(count_for_nechet)