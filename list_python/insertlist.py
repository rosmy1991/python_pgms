sname=[]
length=int(input("enter the size"))
for i in range(length):
   name=input(f"enter position {i}value")
   sname.append(name)

print(sname)
flag=0
cname=input("enter aname")
for i in range(length):
   if (sname[i]==cname):
      sname[i]="anamika"
      flag=1
if(flag==0):
   sname.append("amal")
print("list after modification\n")
print(sname)