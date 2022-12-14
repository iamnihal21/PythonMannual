str = str(input("Enter your string : "))
lst = list(str)
dic = dict()
for i in range (len(lst)) :
    if lst[i] not in dic :
        dic[i]=dic.get(i,0)+1
print(dic.items())