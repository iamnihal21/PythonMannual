import random
state = []
a=int(input('Enter number of item in list : '))
for i in range(0,a) :
    st=eval(input(f'Enter item {i+1} : '))
    state.append(st)
print('Before Shuffling list : ',state)
random.shuffle(state)
print('After Shuffling list : ',state)