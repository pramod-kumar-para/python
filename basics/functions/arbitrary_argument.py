
""" A function can also be called with arbitrary number of arguments
 These arguments will be wrapped inside a tuple
 Before these arbitrary arguments,zero or more normal args may occur
 *args receives a tuple containing the positional arguments beyond
 the formal parameter list"""

def function_name(*args,sep='/'):
    return sep.join(args)

res=function_name("desktop","program files","python34")
print(res)
res=function_name("desktop","program files","python34",sep='-')
print(res)

#  res=function_name("desktop",sep='-',"program files")

""" The above function call results in an error because,
Any formal parameter that occurs after *args must be keyword parameter only
"""
