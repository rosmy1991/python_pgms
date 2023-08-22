#create another list containing nums divisible by 2 and 5
list1=[5,10,2,4,7,15,17]
list2=[]

for i in list1:
    if(i%2!=0 and i%5==0):
        list2.append(i)
print(list1)
print(list2)