
lst=[7,1,2,3,3,5]
lst.sort()
for i in range(0,len(lst)):
    e1=lst[i]
    e2=lst[i+1]
    if(e2-e1 == 0):
            print(e1)
            break  