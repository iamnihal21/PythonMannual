year = eval(input("Enter year : "))
if ((year%400==0) or (year%100!=0) and (year%4==0)) :
    print('This is leap year')
else :
    print('This is Not leap year')