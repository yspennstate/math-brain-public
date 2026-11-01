import itertools, math
import numpy as np


def walsh(m):
    assert m % 4 == 0
    a = np.ones(m) / math.sqrt(m)
    b = np.array([1, -1] * (m // 2), dtype=float) / math.sqrt(m)
    w = np.array([1, 1, -1, -1] * (m // 4), dtype=float) / math.sqrt(m)
    return a, b, w


def build(m, kind, eta=0.0):
    a, b, w = walsh(m)
    A = np.zeros((m + 1, m + 1))
    A[1:, 1:] = np.outer(a, a) + np.outer(b, b)
    if kind == "aligned":
        c = math.sqrt(2) * a
    elif kind == "transverse":
        c = math.sqrt(2) * w
    elif kind == "eta":
        c = math.sqrt(2) * (a + eta * w)
    else:
        raise ValueError(kind)
    A[0, 1:] = c
    A[1:, 0] = c
    return A


def max_pair_det(A):
    ans = 0.0
    for i, j in itertools.combinations(range(len(A)), 2):
        ans = max(ans, abs(np.linalg.det(A[np.ix_([i, j], [i, j])])))
    return ans


def max_cross_rank(A):
    n = len(A)
    ans = 0
    for mask in range(1, 2**n - 1):
        I = [i for i in range(n) if (mask >> i) & 1]
        J = [i for i in range(n) if not ((mask >> i) & 1)]
        ans = max(ans, np.linalg.matrix_rank(A[np.ix_(I, J)], tol=1e-10))
    return ans


m = 8
a, b, w = walsh(m)
G = np.array([[a @ a, a @ b, a @ w], [b @ a, b @ b, b @ w], [w @ a, w @ b, w @ w]])
print("orth_error=", np.max(np.abs(G - np.eye(3))))
for kind in ["aligned", "transverse"]:
    A = build(m, kind)
    eig = np.linalg.eigvalsh(A)
    print(kind, "nonzero_eigs=", eig[np.abs(eig) > 1e-9])
    print(kind, "max_abs_diag=", np.max(np.abs(np.diag(A))))
    print(kind, "max_abs_pair_det=", max_pair_det(A))
    if kind == "aligned":
        print(kind, "max_cross_rank=", max_cross_rank(A))
for eta in [0.0, 0.01, 0.1, 1.0]:
    A = build(m, "eta", eta)
    eig = np.linalg.eigvalsh(A)
    print("eta=", eta, "nonzero_eigs=", eig[np.abs(eig) > 1e-9])
print("mixed_transverse_constant=", 4 * 2**0.25)
print("partner_aligned_constant=", math.pi * math.e)
print("four_pattern_constant=", 4 * math.pi)
print("STATUS=PASS")
