def my_function():
    print("Hello from a function")
my_function()  #only by writing this command the sentence will be printed

def my_fun(fname):
    print(fname + "Refsnes")
my_fun("Emil")
my_fun("Tobias")

#Arbitrary arguments *args
def my_kid(*kids): #if you don't know how many arguments that will be passed into your function add *
    print("The youngest child is " + kids[2])
my_kid("Kamala", "Santosh", "Deepa", "Binod")

#Keyword Argument 
# You can also send arguments with the key = value syntax
# This way the order of the arguments does not matter
def my_child(child3, child2, child1):
    print("The youngest child is "+child3)
my_child(child1="Ram", child3="Shyam", child2="Hanuman")

#Arbitrary Keyword Arguments, **kwargs
#If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_kids(**kid):
    print("his last name is "+ kid["lname"])
my_kids(fname = "Deepa", lname = "Timilsina")

#Default Parameter Value
#If we call the funtion without argument, it uses the default value:
def my_desh(country = "Norway"):
    print("I am from "+country)
my_desh("Sweden")
my_desh()
my_desh("Nepal")

#Passing a list as an argument
def my_food(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
my_food(fruits)

def my_funon(x):
    return 5*x
print(my_funon(3))

def my_fun1(x):
    y = 5*x
    return y
print(my_fun1(5))

def my_fun2(x):
    y = 5*x
    print(y)
my_fun2(6)
my_fun2(2)

def my_fun3(x):
    y = 5 * x
    return y

# Call the function and store the result in a variable
result = my_fun3(6)

# Use the result in another calculation
final_result = result + 10

# Print the final result
print("Final result:", final_result)

def functi ():
    pass

def fun6 (x):
    print(x)
fun6(3)

#To specify that a function can have only positional arguments, add , / after the arguments:
#To specify that a function can have only keyword arguments, add *, before the arguments:
#Combine Positional-Only and Keyword-Only
def my_fntn(a, b, /, *, c, d):
    print(a+b+c+d)
my_fntn(5, 6, c=7, d=8)


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
    print (result)
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

def tri_recursion(k):
  if(k < 6):
    result = k + tri_recursion(k + 1)
    if result>5:
     print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(1)













