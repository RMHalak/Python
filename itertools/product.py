# This tool computes the cartesian product of input iterables.
# It is equivalent to nested for-loops.
# For example, product(A, B) returns the same as ((x,y) for x in A for y in B).

from itertools import product

print(list(product([1,2,3],repeat = 2)))
[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

print(list(product([1,2,3],[3,4])))

A = [[1,2,3],[3,4,5]]
print(list(product(*A)))

B = [[1,2,3],[3,4,5],[7,8]]
print(list(product(*B)))
