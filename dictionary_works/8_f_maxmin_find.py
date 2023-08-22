words=["innnnnnn","hau","g","xx"]
def maxval(words):
    return len(words)
  
print(max(words,key=maxval))
#another method using lambda fun
print(max(words,key=lambda words:len(words)))
print(min(words,key=lambda words:len(words)))















"""def max_num(w):
    return len(w)
print(max(words),key=max_num)"""