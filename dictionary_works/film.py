movies={"2018":5,"keralastory":3,"neymer":4,"kgf":5,"arm":4}
#print(movies["neymer"])
if( movies["neymer"]==4):
    print("hi")
#print all film nmaes
print(movies.keys())
#top rated movie
print(max(movies,key=lambda k:movies.get(k)))

#sort
print(sorted(movies.keys(),key=lambda k:movies.get(k)))
#sort desc
print(sorted(movies.keys(),key=lambda k:movies.get(k),reverse=True))