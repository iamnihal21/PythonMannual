lst = list(map(int ,input ("Enter to ints :").split()))
Combinations=[]
for i in range(len(lst)): 
    for j in range(len(lst)):
        if (i != j) :
            Combinations.append(lst[i])
            Combinations.append(lst[j])
print(Combinations)