#
text="abbc"
dt={}
print(type(dt))
for i in text:
   if i in dt:
       #print("the first recursive letter is",i)
      dt[i]+=1
   else:
      dt[i]=1
print(dt)
print(max(dt.values()))
#print(dt)