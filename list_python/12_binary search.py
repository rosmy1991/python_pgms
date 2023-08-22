lst=[1,2,3,4,5,6,7]
low=0
element=7
up=len(lst)
print(up)
while(low<up):
    mid=low+up//2
    if(element==lst[mid]):
        print("element found")
        break
    elif(element<mid):
        up=mid-1
    elif(element>mid):
        low=mid+1
    else:
        print("not found")