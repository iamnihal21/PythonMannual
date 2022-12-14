import numpy as np 
arr = np.random.randint(0,2,size=(4))
print(arr)
index = []
for i in range(4) :
    for j in range(4) :
        if arr[i] == 1 :
            index.append(i)
            index.append(j)            
print(index)