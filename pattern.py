leng = 1
leng = int(input("Enter n: "))
for i in range(leng):
    count = i + 1
    for j in range(leng - 1 - i):
        print(" ", end="")
    while count > 0:
        print("* ", end="")
        count -= 1
    print("\n")
