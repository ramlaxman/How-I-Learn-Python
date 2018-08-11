myList = [1024, 3, True, 6.5]
# Append Operation
myList.append(False)
print(myList)

# INSERT
myList.insert(2,4.5)
print(myList)

#REMOVE
print(myList.pop())
print(myList)
print(myList.pop(1))
print(myList)
myList.pop(2)
print(myList)

# SORT
myList.sort()
print(myList)

#REVERSE
myList.reverse()
print(myList)

# COUNT
print(myList.count(6.5))

# LOCATION
print(myList.index(4.5))

# REMOVE ELEMENTS
myList.remove(6.5)
print(myList)

# DELETE ELEMENTS USING INDEX OF IT
del myList[0]
print(myList)
