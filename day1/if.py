name = "name"
age = 12
items = [1,2,3,4,5]


# and 
if name.islower() and age.is_integer():
    print("true")
else:
    print("Invalid name or age")

if name.isupper():
    if age.is_integer():
        print("True")
    else:
        print("Invalid age")
else:
    print("invalid name")

# or
if name == "nae" or age == 2:
    print("true")
else: 
    print("None is equal!")

if name.lower():
    print("True")

if not name.lower():
    print("False")

if name == age:
    print("True")

if name == "name":
    print("True")

if name != age:
    print("False")

if 1 in items:
    print("True")

if not (1 in items):
    print("False")
