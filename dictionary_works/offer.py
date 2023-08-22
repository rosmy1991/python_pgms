items=[
    
    {"tea powder":28},
    {"sugar":45},
    {"coffee":67},
    {"dairymilk":170},
    {"kitkat":70},
    {"bourbon":50},
    {"munch":30},
    {"milk":80},
    {"pepsi":99}
]
offer=[
    {"sugar":10},
    {"coffee":20},
    {"milk":5},
    {"pepsi":10}
]

for i in items:
   
   for j in offer:
        #print(j)
        if(i.keys()== j.keys()):
            diff = {key: i[key] - j.get(key)
                       for key in j.keys()}
            print(diff)
            """for m in j.keys():
                a=(i[m]-j.get(m))
                print(a)"""
        else:
            pass
        #print(i.items())
            