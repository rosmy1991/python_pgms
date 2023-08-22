data={"d":"f","r":"l","f":"f","v":"f","a":"l"}

dt={}
for k,v in data.items():
    if v in dt:
        dt[v].append(k)
    else: 
        dt[v]=[k]
print(dt)