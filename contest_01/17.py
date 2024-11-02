line = str(input())

line = line.lower()

if line == line[::-1]:
    print("YES")
else:
    print("NO")