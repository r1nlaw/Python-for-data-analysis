count_number = int(input())

number = list(map(int, input().split()))
len_number = len(number)
summ_unique_numbers = 0

if len_number == count_number:
    number = set(number)

print(len(number))

