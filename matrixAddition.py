import numpy as np

A = np.random.randint(0, 3, size = (5, 5))
B = np.random.randint(0, 3, size = (5, 5))

print("\nMatrix A: ")
for row in A:
    print(row)

print("\nMatrix B: ")
for row in B:
    print(row)

sum = np.array(A) + np.array(B)
print("\nSum: ")
for row in sum:
    print(row)