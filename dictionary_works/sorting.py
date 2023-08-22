num=[3,2,5,1,7,6]

print(sorted(num))
#soring reverse order
print(sorted(num,reverse=True))
#sorting words list
words=["innnnnnn","hau","g","xx"]
print(sorted(words))  # this sorting id based on first alphabet
# we need to sort words on he basis of length of each word
print(sorted(words,key=lambda words:len(words)))
#reverse sorting
print(sorted(words,key=lambda words:len(words),reverse=True))