square = int(input("Enter the size of the pattern: "))
i = 0
while i < square:
    for j in range(square):
        print("*", end="")
    print()
    i +=1
