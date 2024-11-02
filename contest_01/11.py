a, b, c = list(map(int, input().split()))


if abs(b - a) < abs(c - a):
    print(f"B {abs(b - a)}")
else:
    print(f"C {abs(c - a)}")