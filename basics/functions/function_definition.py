
# The keyword def introduces a function definition
# function without return values
def function_name(arguments):
    for i in arguments:
        print(i,end=' ')

function_name(['Hello','github','this','is','me'])

# function with return values
def function_name1(arguments):
    count=''
    for i in arguments:
        count=count+i+' '
    return count

sum=function_name1(['Hello','github','this','is','me'])
print('\n',sum)
