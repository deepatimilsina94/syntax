fruits = ["apple", "mango", "orange", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
     break
for y in "banana":
    print (y)
    #if x == "orange":
       #continue
    #print(x)

for a in range(10):
   print(a)

for q in range(2, 6):
   print(q)

for x in range(2, 30, 3):
   print(x)

for x in range (6):
   #if x == 3: break
   print(x)
else:
   print("Finally finished")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"] #A nested loop is loop inside a loop
for x in adj: #the "inner loop" will be executed one time for each iteration of the "outer loop"
   for y in fruits:
      print(x, y)  #print each adjective for every fruit:

for c in [1,2,4]:
   pass