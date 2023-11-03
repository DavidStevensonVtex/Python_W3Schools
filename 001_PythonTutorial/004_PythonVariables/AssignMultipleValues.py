# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:

# Example

print("Many Values to Multiple Variables")
x, y, z = "Orange", "Banana", "Cherry"
print("x", x)
print("y", y)
print("z", z)

print("One Value to Multiple Variables")
# And you can assign the same value to multiple variables in one line:

# Example
x = y = z = "Orange"
print("x", x)
print("y", y)
print("z", z)


print("Unpack a Collection")
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

# Example
print("Unpack a list:")

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print("x", x)
print("y", y)
print("z", z)
