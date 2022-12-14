houre = eval(input("Enter hours : "))
wage = eval(input("Enter wage : "))
if houre>40 :
    print(40*wage+(houre-40)*wage*1.5)
else :
    print(houre*wage)