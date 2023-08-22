data={"d":"f","r":"l","f":"f","v":"f","a":"l"}

dt={}
for i in data.values():
    if i in dt:
        dt[i]+=1
    else: 
        dt[i]=1
print(dt)
#another method
"""data={"d":"f","r":"l","f":"f","v":"f","a":"l"}
l=list(data.values())
dt={}
for f in l:
    if f in dt:
        dt[f]+=1
    else:
        dt[f]=1
print(dt)"""