
# functions can also be called keyword arguments
# Such arguments are of the form keyword_arg=value
# position of arguments can be altered when you are using keyword arguments

def function_name(name,height,weight):
    print('I\'m ',name)
    print('I\'m ',height,'ft',' tall')
    print('I weigh',weight,' kgs')

function_name(name='Bob',height='5\'10',weight=50)
# position of arguments is altered
function_name(name='Marly',weight=60,height='6\'10')
# position of arguments is altered
function_name(height='7\'10',name='pyscho',weight='50')
# keyword arguments must follow positional arguments
function_name('john','5\'9',66)

# function_name(name='David','5\'9',66)
# This is invalid because of non-keyword argument after keyword only argument
