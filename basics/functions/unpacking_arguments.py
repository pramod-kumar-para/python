__author__ = 'Pramodh'

""" When the arguments are already in the list but needs to be unpacked
for a function call into separate positional arguments, write the
function call with * operator to unpack the list or tuple

dictionaries can deliver keyword arguments with ** operator
*args is called argument unpacking
**args is called keyword argument unpacking
"""

def player_info(name,game,league,country):
    print(name)
    print(game)
    print(league)
    print(country)

d={'name':'Ronaldo','game':'Football','league':'La liga','country':'spain'}
player_info(*d)
player_info(**d)
