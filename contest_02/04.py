def main():
    num = int(input())
    now, max_val, pre = 1, 2, 0
    flag = True
    i = 0

    while i < num:
        for j in range(now):
            i += 1
            print(i, end=" ")
            if i == num:
                break
        print()

        if now - pre == 1 and max_val - now > 0 and flag:
            pre = now
            now += 1
        elif now - pre == 1 and max_val == now:
            max_val += 1
            pre = now
            now -= 1
            flag = False
        elif not flag and pre - now > 0:
            pre = now
            now -= 1
            if now == 0:
                now = pre + 1
                pre = 1
                flag = True

if __name__ == "__main__":
    main()