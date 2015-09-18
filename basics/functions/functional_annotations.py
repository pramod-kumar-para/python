
"""
 Functional annotations gives optional metadata information
 about types used by user defined functions
 Annotations are stored in ..annotations attribute of a function

 Parameter annotations are defined by a colon ':'
 Return type annotations are defined by '->'

 """

def function_name(name:str,age:str) -> str:
    print("annotations",function_name.__annotations__)
    return 'name:'+name+'age'+age

x=function_name('cr7','28')

print(x)
