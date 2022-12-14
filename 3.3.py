p = int(input('Enter P : '))
r = int(input('Enter R : '))
t = int(input('Enter T : '))
n = int(input('Enter n : '))
simpleIntrest = (p*r*t)/100
compoundInterest = p*(1+r/(100*n))**n*t
print('Simple interest is : ',simpleIntrest)
print('Compound interest is : ',compoundInterest)