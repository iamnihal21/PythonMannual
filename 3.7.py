a = int(input('Enter the A : '))
b = int(input('Enter the B : '))
c = int(input('Enter the C : '))
disc = b*b-(4*a*c)
print('Discriminant : ',disc)
rr1 = -b+(b*b-(4*a*c))/2*a
print('Real Roots1 is : ',rr1)
rr2 = -b-(b*b-(4*a*c))/2*a
print('Real Roots2 is : ',rr2)