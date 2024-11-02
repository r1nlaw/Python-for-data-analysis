a, b, c = list(map(int, input().split()))


if a > b:
    temp_max = a
else:
    temp_max = b 

if temp_max > c:
    print(temp_max)
else:
    print(c)