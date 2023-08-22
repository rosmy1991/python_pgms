mobiles=[
    [100,"redminote12",23000,"5g"],
    [101,"oneplusnord",32000,"5g"],
    [102,"iphnoe14",123000,"5g"],
    [103,"s23ultra",133000,"5g"],
    [104,"pexel12",43000,"5g"],
    [105,"nothing",13000,"4g"],
    [106,"galaxya52",23000,"5g"]]
#total number of mobiles
print(len(mobiles))
#all mobile names
"""for i in mobiles:
    print(i[1])"""
#list comprehension
names=[i[1] for i in mobiles]
print(names)
#print 4g mobiles
name1=[i[1] for i in mobiles if(i[3]=="4g")]
print(name1)
#names of mobile prise <30000
name2=[i[1] for i in mobiles if(i[2]<30000)]
print(name2)