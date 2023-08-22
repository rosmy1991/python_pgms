word=["hi","hello","rosmy","hi","hello","hi"]
wd={}
for i in word:
    if i in wd:
        wd[i]+=1
    else:
        wd[i]=1
print(wd)
