thislist = ["apple", "banana", "cherry", "mango", "apple", "avocado", "kiwi"]
print(len(thislist))
print(type(thislist))
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
print(thislist[:4])
print(thislist[3:])
print(thislist[-4:-2])

if "apple" in thislist:
    print("Yes")
thislist[1]="blackcurrant"
print(thislist)

thislist[2:4]=["orange", "pineapple"]
print(thislist)

thislist[4:6]=["potato"]
print(thislist)

thislist.insert(2, "watermelon")
print(thislist)

thislist.append("durian")
print(thislist)

tropical = ["cahsew", "dates"]
thislist.extend(tropical)
print(thislist)

thistuple = ("almond", "chia")
thislist.extend(thistuple)
print(thislist)

thislist.remove("chia")
print(thislist)

thislist.pop(1)
print(thislist)

thislist.pop()
print(thislist)

del thislist[0]
print(thislist)

#del thislist
#print(thislist)
#thislist.clear()
#print(thislist)
for x in thislist:
    print(x)
for i in range(len(thislist)):
    print(thislist[i])
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1
[print(x) for x in thislist]  #list comprehension offers the shortest syntax for looping through lists:

newlist = []
for x in thislist:     #without list comprehension
    if "o" in x:
        newlist.append(x)
print(newlist)

newestlist=[x for x in thislist if "n" in x] #with list comprehesion
print(newestlist) #newlist = [expression for item in iterable if condition == True]

newlylist = [x for x in thislist if x != "orange"]# Only accept items that are not "orange":
print(newlylist)

list1 = [x for x in range(10)]
print(list1)

list2 = [x for x in range(10) if x<5]
print(list2)

list3 = [x.upper() for x in thislist]
print(list3)

list4 = ["hello" for x in thislist]
print(list4)

list5 = [x if x !="watermelon" else "apple" for x in thislist]# "Return the item if it is not watermelon, if it is watermelon return apple".
print(list5)

thislist.sort() #thislist.sort(key = str.lower), case-insensitive sort else capital comes first
print(thislist) 

thislist.sort(reverse = True)
print(thislist)

def myfunc(n):
    return abs(n - 50)
list6 = [100, 50, 65, 82, 23]
list6.sort(key = myfunc)
print(list6)

thislist.reverse()
print(thislist)

mylist = thislist.copy()
print(mylist)

mylist = list(thislist)
print(mylist)

lista = ["a", "b", "c"]
listb = [1, 2, 3]
for x in listb:
    lista.append(x)
print(lista)





    