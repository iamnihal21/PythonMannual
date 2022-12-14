n = int(input('Enter the height of pyramid : '))
n1=n-1
for i in range(0,n) :
    for j in range (0,n1) :
        print(end="  ")
    n1=n1-1
    for j in range(0,i+1) :
        print(" *  ",end=" ")
    print("\n")