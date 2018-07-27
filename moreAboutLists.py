x = [2,3,4,56,8,9,4,2,1,3,4,5]
print(x)

# For appending an extra element to a list
x.append(62)
print(x)

#   Now let's suppose we wan't to insert an element at index(position) 2 which is already filled
x.insert(3, 85)
print(x)

# for removing an element, here in this case it'll remove 1st 4(not speaking of index)
x.remove(4)
print(x)

# for removing any element by index
x.remove(x[5])
print(x)

# for referncing data
print(x[3], x[5])

# slicing up strings
# slicing up means print values falling in a range
# SYNTAX: is x[startElement:endElement]
# here startElement is inclusive but endElement is exclusive
print(x[2:6])
# in this statement 6th element is not printed

# if we wan't to access elements backwards or from the last element
print(x[-4])

# suppose for whatever reason you wan't to access the index value of any elements
print(x.index(85))

# for counting particular no of element in a list
print(x.count(3))

# if we want to sort our list
# just use varName.sort() and then print it, because sort function is actually changing the list right now,
# so it cannot print it instantaneously, so we'll use
x.sort()
print(x)

# if list contains elements as strings, then it'll arrange it in the alphabetical order
y = ['saurabh', 'dinesh', 'sumeet', 'mukul', 'ramesh']
y.sort()
print(y)
