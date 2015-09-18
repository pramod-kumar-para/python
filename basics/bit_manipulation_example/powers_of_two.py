#  finding the powers of 2 in a given list
l=[2,4,6,8,10,16]
def power(l):
    for i in l:
        x=i
        i=i&i-1
        if i==0:
            print(x)
power(l)