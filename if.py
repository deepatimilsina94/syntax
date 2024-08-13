a = 33
b = 200
if b > a:
   print("b is greater than a") # If statement, without indentation (will raise an error):

a = 200
b = 33
if b > a:
   print("b is greater than a")
elif a == b:
   print("a and b are equal")
else:   #The else keyword catches anything which isn't caught by the preceding conditions.
   print("a is greater than b")

if a> b: print("a is greater than b") #Short hand if

a = 2
b = 330     # One line if else statement:
print("A") if a > b else print("B")

x = 41
if x > 10:
   print("above ten,")
   if x > 20:
      print("and also above 20!")
   else:
      print("but not above 20.")

a = 33
b = 200     #if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
if b > a:
   pass

i = 1
while i < 6:
   print(i)
   i +=1
#else: With the else statement we can run a block of code once when the condition no longer is true:
   #print("i is no longer than 6")