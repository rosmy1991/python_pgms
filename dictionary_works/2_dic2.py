car={"name":"swift","brand":"nexa","fueltype":"petrol"}
print(car)
print(car["name"])
print(car.get("brand"))
for i in car:
    print(i,car[i])
car["cost"]=500000
print(car)
print(car.keys())
print(car.values())