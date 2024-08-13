thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
print("banana" not in thisset)

thisset.add("orange")
print(thisset)

tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

thisset.remove("banana")
print(thisset)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2   #join two sets
print(set3)

myset = set1.union(set2, tropical, thisset)
print(myset)

