state = {}
cap = []
def insertion() :
    a=int(input('Enter total state of list : '))
    for i in range(0,a) :
        st=input(f'Enter {i+1} state : ')
        cp=input(f'Enter capital for {i+1} state : ')
        state[st] = cp
        cap.append(state)
    print(state)
    for i,j in state.items() :
        cp=input('Enter capital of {}'.format(i))
        if(cp==state(i)) : 
            print('True')
        else :
            print('False')
insertion()