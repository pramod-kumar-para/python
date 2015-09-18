
questions=['name','age','hobbies']
answers=['python','23','soccer']
index=[0,1,2]

#Entries can be paired with zip function

for q,a,i in zip(questions,answers,index):
    print('{0}  {1} {2}'.format(q,a,i))
