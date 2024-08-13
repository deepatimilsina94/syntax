thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : 1964
}
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

x = thisdict.get("model")
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys() #Add a new item to the original dictionary, and see that the keys list gets updated as well:
print(x) #before the change
car["color"] = "white"
print(x) #after the change

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.items()
print(x)

isdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
isdict["color"] = "red"
print(isdict)


newdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
newdict.update({"year": 2020})
for x in newdict:
    print(x)
    print(thisdict[x])
print(newdict)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)

sdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = sdict.copy()
print(mydict)

thiisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thiisdict)
print(mydict)

myfamily = {
   "child1" :{
      "name": "Emil",
      "year": 2004
   },
   "child2" : {
      "name": "deepa",
      "year" : 1994
   },
   "child3":{
      "name":"arjun",
      "year":1986
   }
}
for x, obj in myfamily.items(): #You can loop through a dictionary by using the items() method like this:
   print(x)
   for y in obj:
      print(y + ":", obj[y])
print(myfamily)
print(myfamily["child2"]["name"])

