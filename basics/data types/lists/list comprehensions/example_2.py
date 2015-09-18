""" A list comprehension consists of brackets containing an expression
 followed by a for clause, then zero or more for or if clauses.
"""
pairs=[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(pairs)