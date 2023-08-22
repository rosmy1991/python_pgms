emp={"id":100,"name":"rosmy","status":"married","salary":500000}
print(type(emp))
print(emp)
#print(emp["name"])
for key in emp:
    print(key,emp[key])
 # adding a new key value pair
emp["gender"]="male"
print(emp)
# updating a value
emp["salary"]=500500
print(emp["salary"])
#using get() method
print(emp.get("salary"))
if("name" in emp):
    print("present")
else:
    print("not present")