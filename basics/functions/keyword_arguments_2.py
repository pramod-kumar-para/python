__author__ = 'Pramodh'
"""
 When a final formal parameter of the name **args is present
 it receives a dictionary of keyword arguments
 except for those corresponding to formal parameters
"""
def function_name(name,height,**info):
    print(name)
    print(height)
    for i in info:
        print(i,":",info[i])

function_name('Pramod',5.10,hobbies='playing football',languages_known='english')

# function_name('Kumar',5.10,hobbies='playing football',
# languages_known='english',name='kumar')

""" The above function call results in TypeError
 Because function got multiple values for argument name
"""