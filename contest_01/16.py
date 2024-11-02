count_number = int(input())

number = list(map(int, input().split()))
len_number = len(number)
summ = 0
final_summ = []
if len_number == count_number:
    for i in range(1, len(number) - 1, 1):
        summ += (number[i - 1] + number[i] + number[i + 1]) / 3
        final_summ += [summ]
        summ = 0
final_summ.insert(0, float(number[0]))
final_summ.append(float(number[-1]))
for value in final_summ:
    print(value, end=" ")

