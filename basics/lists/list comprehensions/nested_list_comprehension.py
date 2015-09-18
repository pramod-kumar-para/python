matrix=[[1,2,3],[2,3,4]]

# list comprehension
l=[row for row in matrix]
print(l)

# nested list comprehension
# The below code gives transpose of a matrix
m=[[row[i] for row in matrix]for i in range(3)]
print(m)

