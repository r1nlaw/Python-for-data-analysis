def main():
    n = int(input())
    result = ""

    while n > 0:
        if n % 26 == 0:
            result = chr(65 + (n - 1) % 26) + result
            n //= 27
            continue

        result = chr(64 + n % 26) + result
        n //= 26

    print(result)

if __name__ == "__main__":
    main()