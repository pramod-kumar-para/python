# else statement is executed by the exhaution of the loop
# else statement is not executed when the loop encounters a break statement

for i in range(0,10):
    if i==5:
        break;
else:
    print('1st loop Else statement in executed')


for i in range(0,5):
    if i==2:
        continue
else:
    print('2nd loop else statement is executed')