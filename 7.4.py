day = {}
temp=[]
def insertion() :
    for i in range(0,7) :
        st=input(f'Enter {i+1} day : ')
        cp=float(input(f'Enter temprature for {i+1} day : '))
        day[st] = cp
        temp.append(day)
    for i,j in day.items():
        if j>40 and j<50 :
            print(i,':',j)
    print(day)
insertion()