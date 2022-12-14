l1 = []
def list() :
    a=int(input('Enter number of item in list : '))
    for i in range(0,a) :
        st=eval(input(f'Enter item {i+1} : '))
        l1.append(st)
    print('Before removing duplicate items list : ',l1)
def newlist() :
    res = [*set(l1)]
    print('List after removing duplicate items : ',res)
list()
newlist()