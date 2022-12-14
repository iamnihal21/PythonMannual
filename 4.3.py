hg = eval(input('Enter your height in m : '))
wg = eval(input('Enter your weight in kg : '))
cal = wg/(hg**2)
if cal<19 :
    print('weak')
elif cal<=25 :
    print('healthy')
else :
    print('Over weight')     