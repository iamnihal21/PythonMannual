n=int(input('Enter the number : '))
def fibo(n):
    if n<=1:
        return n
    else :
        return (fibo(n-1)+fibo(n-2))
fibo(n)
def series() :
    print('Fibonaci Series ↓ ')#for this symbol alt+25(numpad)
    for i in range(n) :
        print(fibo(i),end=" ")    
series()