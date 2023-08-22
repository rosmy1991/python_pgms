#max in list
emli1=[]
length=int(input("Enter the size of list"))
for i in range(0,length):
    num=int(input(f"enter position {i} value"))
    emli1.append(num)
print(emli1)
print(max(emli1))