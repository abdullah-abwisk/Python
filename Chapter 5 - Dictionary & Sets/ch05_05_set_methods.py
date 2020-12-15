b = set()
print(type(b))

# adding values to set
b.add(4)
b.add(5)

print(b)

b.add(5)
# adding 5 once again does not make difference to set

# b.add([4, 5, 6]) cannot add list to set

b.add((2, 3, 4))
# can add tuple to set

# b.add({23:12}) cannot add dictionary to sets

# print set length
print(len(b))

# removing from set
b.remove(5)

print(b.pop())
print(b)