def main():
    s = input()
    rep = 1
    prev = s[0]
    
    for i in range(1, len(s)):
        n = s[i]
        
        if prev == n:
            rep += 1
        else:
            if rep > 1:
                print(f"{prev}{rep}", end="")
            else:
                print(prev, end="")
            rep = 1
            prev = n
    
    if rep > 1:
        print(f"{prev}{rep}", end="")
    else:
        print(prev, end="")
    
    print()

if __name__ == "__main__":
    main()