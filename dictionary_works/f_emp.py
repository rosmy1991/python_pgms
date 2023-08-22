emp={"id":1,"name":"anna","salary":40000}
def name(emp):
    return emp.get("name")
print(name(emp))
#lambda function
name=lambda emp:emp.get("name")
print(name(emp))
sal=lambda emp:emp.get("salary")
print(sal(emp))
#   *args
def add(*args):
    return(sum(args))
print(add(5,10))
addd=lambda *args:sum(args)
print(addd(2,4,5))
#labda fun for finding maximum
maxi=lambda *args:max(args)
print(maxi(3,1,2,5,6,3))
"""def name(emp):
    return emp.get("name")
print(name(emp))
n=lambda emp:emp.get("name")
print(n(emp))
s=lambda emp:emp.get("salary")
print(s(emp))
def add(*args):
    return sum(args)
#lambda
add=lambda *args:sum(args)
print(add(1,2,3))
print(add(3,7))
#lambda fun for finding max value
maximum=lambda *args:max(args)
print(maximum(2,6,3))"""