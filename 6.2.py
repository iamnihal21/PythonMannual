lst =  list(map(float, input("Enter numbers : ").split()))
lst2 = [[x for x in lst if x<0],
        [x for x in lst if x==0],
        [x for x in lst if x>0]]
print("Positive :",len(lst2[2])," Zero :",len(lst2[1])," Negetive :",len(lst2[0]))