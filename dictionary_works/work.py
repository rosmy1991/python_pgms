text="abbccdddddssaa"
wc={}
for i in text:
    if i in wc:
        wc[i]+=1
    else:
        wc[i]=1
x=max(wc,key=lambda s:wc.get(s))
print(x)