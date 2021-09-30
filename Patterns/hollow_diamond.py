rows = int(input("Enter Hollow Diamond Pattern Rows = "))
#loop for upper half hollow diamond
for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(end = ' ')
    for k in range(1, 2 * i):
        if k == 1 or k == i * 2 - 1:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()
#loop to print lower half hollow diamond 
for i in range(rows-1,0, -1):
    for j in range(1,rows-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
