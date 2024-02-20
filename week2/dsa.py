# LIST or ARRAYS
array = ["apple", "mango", "banana", "pawpaw"]

array.sort(reverse=False)
array.count("apple")
array.append("nuts")
array.extend("apples")
new_arr = array.pop()  # removes last item
array.remove("apple")  # removes given item
array.reverse()


# SET
s1 = {1, 2, 3, 4, 5}
s2 = {5, 6, 7, 8, 9}
print(type(s1))

s1.add(6)
print(s)

c = s1.copy()
s1.add(7)
s1.clear()
s = c.copy()
dif = s1.difference_update(s1, s2)
print(dif)

s1.discard(6)
print(s1)

s1.remove(5)
print(s1)

ans = s1.union(s2)
print(ans)
print("s >", s)
print("C >", c)

# DICTIONARY
data = {
    "key": "value",
    "name": "john",
    "age": 12,
    "is_male": True,
}

da = data.fromkeys(["name", "age"])
print(da)


# TUPLE
tups = (1, 1, 1, 3, 2, 3, 4)
print(tups)
print(tups.index(4))
