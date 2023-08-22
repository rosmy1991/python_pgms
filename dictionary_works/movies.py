movies=[
    {"language":"malayalam","name":"2018","rating":5,"year":2023,"genres":["mystery"]},
    {"language":"malayalam","name":"aadujeevitahm","rating":5,"year":2023,"genres":["fiction","drama"]},
    {"language":"malayalam","name":"neymar","rating":4,"year":2023,"genres":["action","comedy","romance"]},
    {"language":"malayalam","name":"sunny","rating":4,"year":2022,"genres":["drama","thriller"]},
    {"language":"malayalam","name":"12th man","rating":3,"year":2022,"genres":["drama","thriller"]},
    {"language":"thamil","name":"vikram","rating":5,"year":2022,"genres":["action","thriller"]},
    {"language":"thamil","name":"jai bhim","rating":5,"year":2021,"genres":["mystery","crime"]},
    {"language":"hindi","name":"pathaan","rating":5,"year":2023,"genres":["action","thriller"]},
    {"language":"telungu","name":"kgf","rating":15,"year":2018,"genres":["action","romance","thriller"]}

]
#MOVIES RELEASED IN 2022
"""for i in movies:
    if( i.get("year")==2022):
        print(i.get("name"))
print("............................................................")
#print All movie names.........................
for i in movies:
    print(i.get("name"))
#list comprehention
movie_names=[i.get("name") for i in movies]
print(movie_names)
print("............................................................")
#movies with drama genres............................... 

for i in movies:
    if  "mystery" in i.get("genres"):
        print(i.get("name"))
for i in movies:
    if "drama" in i.get("genres"):
        print(i.get("name"))
print("............................................................")
#list comprehention
mv=[i.get("name") for i in movies if "drama" in i.get("genres")]
print(mv)
#top rated movies.............................."""

print(max(movies,key=lambda k:k.get("rating")))
#malayalam movies......................
"""for i in movies:
    if "malayalam" in i.get("language"):
         print(i.get("name"))
#MOVIES RELEASED IN 2022
for i in movies:
    if( 2022 in i.get("year")):
        print(i.get("name"))"""