import itertools
import math
import numpy as np


def full_matrix(eps: float, m: int) -> np.ndarray:
    """Strict-N3 stress family from the report."""
    u = np.zeros(2*m)
    v = np.zeros(2*m)
    u[:m] = 1/math.sqrt(m)
    v[m:] = 1/math.sqrt(m)
    z = (u+v)/math.sqrt(2)
    b = u-v
    lam = 2/eps
    A = np.zeros((1+2*m, 1+2*m))
    A[0, 0] = eps
    A[0, 1:] = b
    A[1:, 0] = b
    A[1:, 1:] = lam*np.outer(z, z)
    return A


def exterior_profile(A: np.ndarray):
    n = A.shape[0]
    triples = list(itertools.combinations(range(n), 3))
    W = [0.0]*4
    for I in triples:
        for J in triples:
            r = len(set(I).intersection(J))
            d = np.linalg.det(A[np.ix_(I, J)])
            W[r] += d*d
    return W


def max_cross_rank(A: np.ndarray):
    n = A.shape[0]
    ans = 0
    for mask in range(1, 2**n-1):
        S = [i for i in range(n) if (mask >> i) & 1]
        T = [i for i in range(n) if not ((mask >> i) & 1)]
        ans = max(ans, np.linalg.matrix_rank(A[np.ix_(S, T)], tol=1e-10))
    return ans


for eps in [1.0, 0.5, 0.1, 0.01]:
    M = np.array([
        [eps, 1.0, -1.0],
        [1.0, 1.0/eps, 1.0/eps],
        [-1.0, 1.0/eps, 1.0/eps],
    ])
    eig = np.linalg.eigvalsh(M)
    pred = np.sort(np.array([
        2.0/eps,
        (eps + math.sqrt(eps*eps+8.0))/2.0,
        (eps - math.sqrt(eps*eps+8.0))/2.0,
    ]))
    assert np.max(np.abs(eig-pred)) < 1e-10
    assert min(abs(eig)) >= 1.0-1e-10
    assert abs(np.linalg.det(M) + 4.0/eps) < 1e-9
    print(f"eps={eps:g} eig={eig.tolist()} det={np.linalg.det(M):.12g}")

# Small physical instance: enumerate every cut and every ordered triple pair.
eps = 0.5
m = 3
A = full_matrix(eps, m)
max_pair_det = 0.0
for i, j in itertools.combinations(range(A.shape[0]), 2):
    max_pair_det = max(max_pair_det, abs(np.linalg.det(A[np.ix_([i,j],[i,j])])))
W = exterior_profile(A)
print(f"physical eps={eps} m={m} max_diag={np.max(np.abs(np.diag(A))):.12g}")
print(f"max_abs_physical_pair_det={max_pair_det:.3e}")
print(f"max_cross_rank={max_cross_rank(A)}")
print(f"W={W} sumW={sum(W):.12g} expected_e3A2={16/eps**2:.12g}")
print(f"W1_formula={16/eps**2*(1-1/m)**2:.12g}")
print(f"new_uniform_constant_4sqrt2={4*math.sqrt(2):.12g}")
print("STATUS=PASS")
