rows = int(input("Enter number of rows: "))

# ----------- NORMAL PYRAMID -----------
print("\nNormal Pyramid:")
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# ----------- REVERSE PYRAMID -----------
print("\nReverse Pyramid:")
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

    
    
