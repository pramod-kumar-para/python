
# creating an empty list
squares=[]

for i in range(1,10):
    squares.append(i*i)

print(squares)
#The above snippet creates a variable named i,that exists even after the loop terminates
# Therefore to avoid such side effects,use lambda expression

l=[1,2,3,4,5]
squares=list(map(lambda x:x*x,l))
print(squares)

# You can also use the following statement as a alternative
# >>> squares=[x**2 for x in range(10)]

