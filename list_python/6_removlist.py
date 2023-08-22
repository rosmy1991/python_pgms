birds=["peacock","pigeon","duck","hen"]
ch_bird=input("Enter a bird")
#for i in birds:
#    if i==ch_bird:
#        birds.remove(i)
#print(birds)
for i in range(len(birds)):  # another for loop method
    if birds[i]==ch_bird:
        birds.remove(birds[i])
print(birds)