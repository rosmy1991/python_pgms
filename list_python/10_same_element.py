#find the common elements in 2 lists
list1=[8,9]
list2=[4,7,8,9]
p1=0
p2=0
print
while(p1<len(list1) and p2<len(list2)):
    if(list1[p1]==list2[p2]):
        print(list1[p1])
        p1+=1
    elif(list1[p1]<list2[p2]):
        p1+=1
    elif(list1[p1]>list2[p2]):
        p2+=1
