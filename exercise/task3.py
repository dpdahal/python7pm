num = int(input("Enter any number: "))

for i in range(1, 11):
    for j in range(1, num + 1):
        # print(("{:8d}").format(i* j), end="")
        print(f"{i * j}", end=" ")
    print("\t \t")
