Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
length = 9
width = 6
perimeter = 2* (length + width)
print("perimeter of a rectangle is ",perimeter)
perimeter of a rectangle is  30
print("Python is great, it's wild!")
Python is great, it's wild!
print("2 to the 10th power is " , 2**10)
2 to the 10th power is  1024
import math
result = math.factorial(7) - math.factorial(5)
print("7 factorial minus 5 factorial is ",result)
7 factorial minus 5 factorial is  4920
output = Siron*5
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    output = Siron*5
NameError: name 'Siron' is not defined
str Siron
SyntaxError: invalid syntax
str siron
SyntaxError: invalid syntax
myname = "Siron"
output = myname*5
print("output")
output
myname="Siron"
output =  myname*5
print(output)
SironSironSironSironSiron
>>> Name = "Siron"
>>> outcome = name.ljust(15)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    outcome = name.ljust(15)
NameError: name 'name' is not defined. Did you mean: 'Name'?
>>> Name = 15
>>> outcome = Name.ljust(15)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    outcome = Name.ljust(15)
AttributeError: 'int' object has no attribute 'ljust'
>>> name = "Siron"
>>> print(f"name:<15")
name:<15
>>> name = "Siron"
>>> print(f"{name:<15}")
Siron          
>>> name = "Siron"
\
>>> print(f"{name:<15}.")
Siron          .
>>> 
>>> import math
>>> PI = math.PI
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    PI = math.PI
AttributeError: module 'math' has no attribute 'PI'
>>> print("PI to 5 decimal places: ",format(math.pi,".5f"))
PI to 5 decimal places:  3.14159
>>> print("Integer value of 7.2: ", int(7.2))
Integer value of 7.2:  7
>>> name = input("Enter your name: ")
Enter your name: Siron
>>> unicode_values = [ord(char) for char in name]
>>> print("Unicode values: ",unicode_values)
Unicode values:  [83, 105, 114, 111, 110]
