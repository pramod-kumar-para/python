
# A tuple consists of number of values separated by commas

t=12,23,45,'str'
print(t)
# nested tuples are also possible

q=1,2,t
print(q)

# a tuple with single element is created by following a value with comma
x=1,
print(x)

# tuples can be accessed by indexing or slicing
for i in range(0,4):
    print(t[i])         #indexing

print(t[:])             #slicing

# Its not possible to assign to individual values of a tuple
# But its possible to assign to mutable objects such as lists in a tuple

t=[1,2,3],'hello','world'
t[0][0]=4
t[0][1]=5
print(t)


