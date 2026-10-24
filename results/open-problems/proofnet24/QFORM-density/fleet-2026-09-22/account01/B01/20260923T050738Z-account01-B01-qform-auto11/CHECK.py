import itertools
import math
import numpy as np

rng = np.random.default_rng(230923)
max_w1_error = 0.0
max_cut_error = 0.0

for _ in range(50):
    n = 7
    G = rng.normal(size=(n, n))
    A = (G + G.T) / 2
    s = 0
    if abs(A[s, s]) < 0.2:
        A[s, s] += 1.0
    a = A[s, s]
    K = list(range(1, n))
    B = A[np.ix_(K, K)] - np.outer(A[K, s], A[s, K]) / a

    pairs = list(itertools.combinations(range(len(K)), 2))
    D0 = 0.0
    W1 = 0.0
    for P in pairs:
        for T in pairs:
            if set(P).isdisjoint(T):
                db = np.linalg.det(B[np.ix_(P, T)])
                D0 += db * db
                H = [s] + [K[i] for i in P]
                U = [s] + [K[i] for i in T]
                da = np.linalg.det(A[np.ix_(H, U)])
                W1 += da * da
    max_w1_error = max(max_w1_error, abs(W1 - a * a * D0) / (1 + abs(W1)))

    cut_values = []
    for mask in range(1 << len(K)):
        I = [i for i in range(len(K)) if (mask >> i) & 1]
        J = [i for i in range(len(K)) if not ((mask >> i) & 1)]
        e2 = 0.0
        if len(I) >= 2 and len(J) >= 2:
            for P in itertools.combinations(I, 2):
                for T in itertools.combinations(J, 2):
                    d = np.linalg.det(B[np.ix_(P, T)])
                    e2 += d * d
        cut_values.append(e2)
    avg = float(np.mean(cut_values))
    max_cut_error = max(max_cut_error, abs(avg - D0 / 16) / (1 + abs(D0)))

C_E2 = 12 * 2 ** (5 / 6) * math.exp(5 / 24)
C_overlap = math.sqrt(2) * C_E2
C_linear_p3 = 8 * 2 ** (3 / 8) * math.sqrt(3) / 3

B0 = np.array([[0.0, 0.0, 1.0], [0.0, 0.0, 0.0], [1.0, 0.0, 0.0]])
K0 = np.array([[1.0, 0.0], [0.0, 1.0], [0.0, 0.0]])
A0 = np.block([[B0, K0], [K0.T, np.zeros((2, 2))]])
eigs = np.linalg.eigvalsh(A0)
v = np.array([0.0, 0.0, 1.0])
c = B0 @ v - (v @ B0 @ v) * v
Delta = np.prod(np.linalg.svd(K0, compute_uv=False)[:2])

print('max_W1_identity_relative_error', repr(max_w1_error))
print('max_partition_expectation_relative_error', repr(max_cut_error))
print('C_E2', repr(C_E2))
print('C_overlap', repr(C_overlap))
print('C_linear_transverse_p3', repr(C_linear_p3))
print('stress_eigenvalues', [round(float(x), 12) for x in eigs])
print('stress_Delta', Delta)
print('stress_d', abs(v @ B0 @ v), 'stress_g', np.linalg.norm(c))
print('STATUS=PASS')
