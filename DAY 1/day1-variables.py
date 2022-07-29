# 100 Days of Python
# Cole Catron

input("What is your name? ")
# The argument will be passed, but the data WILL NOT be stored
# anywhere and will be deleted from RAM

name = input("What is your name? ")
print("Hello " + name + "!\n")
# The input() function is being assigned to the string variable
# called "name"
#
# The print() function prints the contents of the variable "name",
# which contains the string that the user inputs into the variable

name = "Juan"
print("Hello " + name + "!")
# prints "Juan"

name = "Angela"
print("Hello " + name + "!\n")
#prints "Hello Angela"

name = input("What is your name? ")
length = len(name)
print(length)
# Input for the name is stored in the variable "name"
# 
# The len() function will store the integer into the variable named
# "length", which will be an integer value
#
# The print() will print what is in the "length" variable, which is
# a numerical value