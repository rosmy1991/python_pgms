word1="abcd"
word2="ac"
wc={}
is_kangaroo=True
for i in word1:
    if i in wc:
        wc[i]+=1
    else:
        wc[i]=1
for j in word2:
    if j in wc and wc[j]>0:
        wc[j]-=1
    else:
        is_kangaroo=False
        break
print(is_kangaroo)
