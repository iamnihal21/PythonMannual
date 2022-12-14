n1 = 5
n2 = 10
n3 = 15
mx = (n1 if (n1 > n2 and n1 > n3) else
	(n2 if (n2 > n1 and n2 > n3) else n3))
print('Maximum is : ',mx)