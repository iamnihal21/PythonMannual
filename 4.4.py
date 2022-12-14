grade = eval(input('Enter your marks : '))
def switch(grade) :
    if grade>=90 :
        return "A"
    elif grade>=80 and grade<=89 :
        return "B"
    elif grade>=70 and grade<=79 :
        return "C"
    elif grade>=60 and grade<=69 :
        return "D"
    elif grade>=50 and grade<=59 :
        return "E"
    else: 
        return "F"
print(switch(grade))    