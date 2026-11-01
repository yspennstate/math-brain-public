import itertools
import numpy as np

rng = np.random.default_rng(0)
n = 7
A = rng.normal(size=(n, n))
A = (A + A.T) / 2
trip = list(itertools.combinations(range(n), 3))

C3_minor = sum(float(np.linalg.det(A[np.ix_(S, T)]) ** 2) for S in trip for T in trip)
sv = np.linalg.svd(A, compute_uv=False)
C3_spectral = sum(float((sv[i] ** 2) * (sv[j] ** 2) * (sv[k] ** 2))
                  for i, j, k in itertools.combinations(range(n), 3))
D3 = sum(float(np.linalg.det(A[np.ix_(S, T)]) ** 2)
         for S in trip for T in trip if set(S).isdisjoint(T))

cut_values = []
row_delete_violations = []
for mask in range(1 << n):
    I = [i for i in range(n) if (mask >> i) & 1]
    J = [i for i in range(n) if not ((mask >> i) & 1)]
    M = A[np.ix_(I, J)]
    Z3 = 0.0
    if len(I) >= 3 and len(J) >= 3:
        for S in itertools.combinations(range(len(I)), 3):
            for T in itertools.combinations(range(len(J)), 3):
                Z3 += float(np.linalg.det(M[np.ix_(S, T)]) ** 2)
        for ii in range(len(I)):
            star = 0.0
            for S in itertools.combinations(range(len(I)), 3):
                if ii in S:
                    for T in itertools.combinations(range(len(J)), 3):
                        star += float(np.linalg.det(M[np.ix_(S, T)]) ** 2)
            N = np.delete(M, ii, axis=0)
            Z2 = 0.0
            if N.shape[0] >= 2 and N.shape[1] >= 2:
                for S in itertools.combinations(range(N.shape[0]), 2):
                    for T in itertools.combinations(range(N.shape[1]), 2):
                        Z2 += float(np.linalg.det(N[np.ix_(S, T)]) ** 2)
            rhs = float(np.dot(M[ii], M[ii])) * Z2
            row_delete_violations.append(star - rhs)
    cut_values.append(Z3)

print("C3_minor", repr(C3_minor))
print("C3_spectral", repr(C3_spectral))
print("C3_error", repr(abs(C3_minor - C3_spectral)))
print("D3", repr(D3))
print("avg_cut_Z3", repr(sum(cut_values) / (1 << n)))
print("D3_over_64", repr(D3 / 64))
print("cut_error", repr(abs(sum(cut_values) / (1 << n) - D3 / 64)))
print("max_row_delete_violation", repr(max(row_delete_violations)))
