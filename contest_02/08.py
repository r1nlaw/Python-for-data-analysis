number1, number2 = list(map(str, input().split()))

sort_number1 = ''.join(sorted(number1))
sort_number2 = ''.join(sorted(number2))

if sort_number1 == sort_number2:
    print("YES")
else:
    print("NO")
