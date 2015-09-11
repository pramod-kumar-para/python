__author__ = 'Pramodh'

""" Python supports the creation of anonymous functions at runtime using
 a construct called lambda
"""

g=lambda x:x+2
print(g(39))

square =lambda n:n*n
print(square(10))

cube=lambda n:n*n*n
print(cube(10))

sum = lambda x,y:x+y
print(sum(2,3))

l=[1,2,3,4,5]
squares=list(map(lambda x:x*x,l))
print(squares)



