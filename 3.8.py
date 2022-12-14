from math import *
height = int(input("Insert height :  "))
angle =  int(input("Insert Angle :  "))
angler = ((pi / 180) * angle)
length = (height / sin(angler))
print("The length of ladder required is ", length)