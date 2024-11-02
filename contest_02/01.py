count_number = int(input())
line_for_number = list(map(int, input().split()))
dictionary = {}
if count_number == len(line_for_number):
    for item in line_for_number:
        if item in dictionary :
            dictionary[item] += 1
        else:
            dictionary[item] = 1

max_count_for_number = max(dictionary.values())
for key, value in dictionary.items():
    if value == max_count_for_number:
        print(key)


