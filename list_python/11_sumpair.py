#we have a list and find a pair of values that 
#linear method
"""list1=[5,2,6,3,4]
sum=7
for i in list1:
    for j in list1:
        if(i!=j and i<j):
            if(sum==i+j):
                print(i,j)"""
#another easy method
lst=[1,2,3,4,5,6]
sum=7
low=0
upper=len(lst)-1
while(low<upper):
    cur_sum=lst[low]+lst[upper]
    if(cur_sum==sum):
        print(lst[low],lst[upper])
        low+=1
    elif(cur_sum<sum):
        low+=1
    elif(cur_sum>sum):
        upper-=1
        
