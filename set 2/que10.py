tuple1 = (11, [22, 33], 44, 55)

# Convert the tuple to a list
list1 = list(tuple1)

# Modify the first item of the list
list1[1][0] = 222

# Convert the list back to a tuple
tuple1 = tuple(list1)

print(tuple1)
