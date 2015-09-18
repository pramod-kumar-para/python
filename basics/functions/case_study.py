#"Default parameters are evaluated only once"

#"consider the following example"

def add_elements(a,l=[]):
    l.append(a)
    return l

"""A new list is created once when the function is defined,
    and the same list is used in each successive call.
"""
print(add_elements(1))
print(add_elements(2))


"""Therefore in order to create a new object each time
    a function is called do the following"""

def add_elements1(a,l=None):
    if l is None:
        l=[]
    l.append(a)
    return l
print(add_elements1(1))
print(add_elements1(2))

