N = int(input())
count5000 = 0
count1000 = 0
count500 = 0
count200 = 0
count100 = 0

while N != 0:
    if N >= 5000:
        N -= 5000
        count5000 += 1
    if N < 5000 and N >= 1000:
        N -= 1000
        count1000 += 1
    if N < 1000 and N >= 500:
        N -= 500
        count500 += 1
    if N < 500 and N >= 200:
        N -= 200
        count200 += 1
    if N < 200 and N >= 100:
        N -= 100
        count100 += 1
print(f"{count5000} {count1000} {count500} {count200} {count100}")

