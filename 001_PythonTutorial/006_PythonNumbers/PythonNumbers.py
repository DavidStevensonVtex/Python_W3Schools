# Python Numbers
print("Python Numbers")
# There are three numeric types in Python:

# int
# float
# complex
# Variables of numeric types are created when you assign a value to them:

# Example
x = 1  # int
y = 2.8  # float
z = 1j  # complex

# To verify the type of any object in Python, use the type() function:

# Example
print("x", type(x))
print("y", type(y))
print("z", type(z))

# x <class 'int'>
# y <class 'float'>
# z <class 'complex'>

print("\nInt")
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

# Example
# Integers:

x = 1
y = 35656222554887711
z = -3255522

print("x", type(x))
print("y", type(y))
print("z", type(z))
# x <class 'int'>
# y <class 'int'>
# z <class 'int'>

print("\nFloat")
# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

# Example
# Floats:

x = 1.10
y = 1.0
z = -35.59

print("x", type(x))
print("y", type(y))
print("z", type(z))
# x <class 'float'>
# y <class 'float'>
# z <class 'float'>

print("\nFloat can also be scientific numbers with an 'e' to indicate the power of 10.")

# Example
# Floats:

x = 35e3
y = 12e4
z = -87.7e100

print("x", x, type(x))
print("y", y, type(y))
print("z", z, type(z))
# x 35000.0 <class 'float'>
# y 120000.0 <class 'float'>
# z -8.77e+101 <class 'float'>


print("\nComplex")
# Complex numbers are written with a "j" as the imaginary part:

# Example
# Complex:

x = 3 + 5j
y = 5j
z = -5j

print("x", x, type(x))
print("y", y, type(y))
print("z", z, type(z))
# x (3+5j) <class 'complex'>
# y 5j <class 'complex'>
# z (-0-5j) <class 'complex'>


print("\nType Conversion")
# You can convert from one type to another with the int(), float(), and complex() methods:

# Example
# Convert from one type to another:

x = 1  # int
y = 2.8  # float
z = 1j  # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print("a", a, type(a))
print("b", b, type(b))
print("c", c, type(c))

# Type Conversion
# a 1.0 <class 'float'>
# b 2 <class 'int'>
# c (1+0j) <class 'complex'>


# Random Number
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

# Example
# Import the random module, and display a random number between 1 and 9:

import random

print("random 1 to 10", random.randrange(1, 10))

# In our Random Module Reference you will learn more about the Random module.
# https://www.w3schools.com/python/module_random.asp
