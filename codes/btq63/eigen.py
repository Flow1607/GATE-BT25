import numpy as np

k = float(input("Enter k: "))
A = np.array([[1, 0, 1],
              [0, k, 0],
              [3, 0, -1]])
eigs = np.sort(np.linalg.eigvals(A))

print("Eigenvalues:", eigs)
print("Matches [-2, 1, 2]:", np.allclose(eigs, [-2, 1, 2]))