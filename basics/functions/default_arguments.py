__author__ = 'Pramodh'

# By providing default arguments
# we can provide only mandatory values during function calls
# This function can be called in several ways
# giving the mandatory args
# giving one of the optional args along with mandatory args
# or giving all the args

def function_name_1(height,name='pramod'):
    print(name,end='\n')
    print('Height is ',height)

function_name_1(5.10)
function_name_1(4.10,'kumar')


def function_name_2(name='Ronaldo',Hobbies=['Football','soccer'],Location='spain'):
    print('I\'m ',name,end='\n')
    print('My hobbies are playing ',end=' ')
    for i in Hobbies:
        print(i,end=' ')
    print('\nIm from',Location)

function_name_2()
function_name_2('Kumar',['ping pong','gaming'],'India')
