
person = {'name':'python','age':23}
person['gender']='male'

print(list(person.keys()))

del person['age']
# returns a list of keys in arbitrary order
print(list(person.keys()))

# returns a list of keys in sorted order
print(sorted(list(person.keys())))

# membership checking in dictionaries using in keyword

print('name' in person)
