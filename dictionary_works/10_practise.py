#most recursive letter...........................
"""text="abbaaccccc"
wc={}
for i in text:
    if i in wc:
        wc[i]+=1
    else:
        wc[i]=1

print(wc)
print(max(wc,key=lambda k:wc.get(k)))
#most lengthy word in a list.....................
words=["ji","fgagggg","hai","hhhhhhhhhh"]
print(max(words,key=lambda k:len(k)))
#sorting..............................
words=["ji","fgagggg","hai","hhhhhhhhhh"]
aa=sorted(words,key=lambda i:len(i))
ab=sorted(words,key=lambda i:len(i),reverse=True)
print(aa)
print(ab)"""
a={"aaa":3}
k,v=(a.key(),a.values())
print(k,v)