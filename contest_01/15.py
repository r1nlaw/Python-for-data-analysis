line = str(input())
line = line.replace(";", " ")
line = line.split()
line = list(map(int, line))
count_for_number = 0
summ = 0
for i in range(0, len(line), 1):
    count_for_number += 1
    summ += line[i]

final_summ = summ / count_for_number

print(final_summ)
