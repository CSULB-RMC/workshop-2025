'''
Problem 1: Variables
'''
print("Section 1: Variables")
# Integer
x = 1
print(x)

# Strings
x = "Hello World"
print(x)

# List
myList = [5, 6, 7]
print(myList[2])
'''
Problem 2: Conditionals

Booleans: True or False
'''
print("\nSection 2: Conditionals")
# Booleans
b = True
if b:
  print("True")
else:
  print("False")
x = 2
y = 2
if x == 5 or y == 2:
  print("True")

print(x > 10)
print(y <= 2)
'''
Problem 3: Loops

Deterministic Loops vs Dynamic Loops

Starts and ends iterations based on a boolean
'''
print("\nSection 3: Loops")
print("For Loop")
for i in range(0, 10):
  print(i)

print("\nFor Each")
list = [1, 2, 3]
for element in list:
  print(element)

print("\nEnumerate")
for index, element in enumerate(list):
  print(index, element)

print("\nWhile Loop")
while (True):
  print(x)
  break
'''
Problem 4: Classes
'''
print("\nSection 4: Classes")


class MyClass:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def add(self):
    return self.x + self.y

  def __str__(self):
    return "MyClass: " + str(self.x) + " " + str(self.y)


c = MyClass(1, 2)
print(c.add())
print(c)

print("section 5: Algggg")
n = [0 for i in range(1000)]
for i in n:  # O(n)
  print(i)
# for j in n:  # O(n)
#       print(i, j)
#   for k in n:  # O(n)
#      print(i, j, k)  # total O(n^3)

if 100 in n:  # O(n)
  print("found")
else:
  print("Not Found")
n.sort()  # nlogn
print(n)
