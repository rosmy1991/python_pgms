from json import load
with open("C:\\Users\\ferdinant\\AppData\\Local\\Programs\\Python\\Python311\\luminar\\dictionary_works\\jsonpgms\\mdb.json","r") as f:
    data=load(f)
#total number of movies
#print(len(data))
#movie names
# for i in data:
#     print(i.get("title"))
# m_nam=[i.get("title")for i in data]
# print(m_nam)
#movie ith highest run time
# m_m=max(data,key=lambda s:int(s.get("runtime")))
# print(m_m.get("title"))
#print all genres...................................................
# m_genres=set()
# for i in data:
#     #print(i.get("genres"))
#     m_genres.update(i.get("genres"))
# print(m_genres)
#another method.....................
# m_genres={j for i in data for j in i.get("genres")}
# print(m_genres)
#movie-comedy..................
# for i in data:
#     if "Comedy" in i.get("genres"):
#         print(i.get("title"))
# #list comprehension
# mm=[i.get("title")for i in data if "Comedy" in i.get("genres")]
# print(mm)
# #movie-comedy or fantacy..................
mmm={i.get("title")for i in data for j in i.get("genres") if j in ["Comedy","Fantasy"]}

print(mmm)