# Implementation of stack ADT
class stack:
    MAX=10
    def __init__(self,top=-1,l=None):
        self.l=[]
        self.top=top 
    def push(self):
        if self.top==self.MAX-1:
            print('stack overflow')
        else:
            x=input('enter the element to insert')
            self.top+=1
            self.l.append(x)
    def pop(self):
        if self.top==-1:
            print('stack underflow')
        else:
            print('popped element is ',self.l[self.top])
            self.l.remove(self.l[self.top])
            self.top-=1
    def display_stack(self):
        print('elements of stack are',self.l)

x=stack()
for i in range(11):
    x.push()
for i in range(5):
    x.pop()
x.display_stack()



    
