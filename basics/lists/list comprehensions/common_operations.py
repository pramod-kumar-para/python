numbers=[1,2,3]
strings=["str","pop"]

# appends a new item to the end of the list
numbers.append(4)
print(numbers)

# removes an item from the end of the list,and return it
print(numbers.pop())
print(numbers)

# extends the list be appending all items in given list
numbers.extend(strings)
print(numbers)

# removes the first item from the list,whose values is argument
numbers.remove('str')
print(numbers)

# returns a shallow copy of the llist
strings=numbers.copy()
print(strings)

# return the index in the list of the first item whose value is argument
print(numbers.index('pop'))

# counts number of times argument appears in the list
print(numbers.count(1))

# sorts the given list
numbers=[1,2,3,4]
numbers.sort(key=None,reverse=True)
print(numbers)
numbers.sort(key=None,reverse=False)
print(numbers)

# reverse the elements of the list
numbers.reverse()
print(numbers)


#clears the entire list
numbers.clear()
print(numbers)


