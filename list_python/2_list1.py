##add max element+10 in second position
em=[]
length=int(input("Enter the size of list"))
for i in range(0,length):
    num=int(input(f"enter position {i} value"))
    em.append(num)
m=max(em)
em.insert(2,m+10)
print(em)