text="abbaacc"
wc={}
for ch in text:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1
print(wc)
print("most recursive letter")
print(max(wc,key=lambda w:wc.get(w)))
print("least recursive letter")
print(min(wc,key=lambda w:wc.get(w)))