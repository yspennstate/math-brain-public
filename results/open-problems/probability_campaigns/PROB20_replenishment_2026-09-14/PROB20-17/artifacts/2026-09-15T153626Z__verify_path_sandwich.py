import itertools
import numpy as np
from collections import Counter


def opn(M):
    return np.linalg.svd(M, compute_uv=False)[0]


def rand_psd(d, rng):
    Q, _ = np.linalg.qr(rng.normal(size=(d, d)))
    vals = np.exp(rng.uniform(-5.0, 2.0, size=d))
    return Q @ np.diag(vals) @ Q.T


def chain_rhs(A):
    rhs = opn(A[0]) * opn(A[-1])
    for j in range(len(A) - 1):
        rhs *= opn(A[j] @ A[j + 1])
    return rhs


rng = np.random.default_rng(20260915153626)
worst_chain = 0.0
for m in range(2, 9):
    for _ in range(300):
        A = [rand_psd(4, rng) for __ in range(m)]
        W = A[0]
        for X in A[1:]:
            W = W @ X
        lhs = opn(W) ** 2
        rhs = chain_rhs(A)
        ratio = lhs / rhs if rhs else 0.0
        worst_chain = max(worst_chain, ratio)
        assert lhs <= rhs * (1 + 1e-9) + 1e-9
print('chain theorem random max lhs/rhs =', worst_chain)

# Exact n=4 Hamiltonian-path corollary derived from the theorem + scalar Cauchy.
for _ in range(500):
    A = [rand_psd(4, rng) for __ in range(4)]
    S = 0.0
    H = 0.0
    a = [opn(X) for X in A]
    p = np.zeros((4, 4))
    for i in range(4):
        for j in range(i + 1, 4):
            p[i, j] = p[j, i] = opn(A[i] @ A[j])
    for sig in itertools.permutations(range(4)):
        i, j, k, l = sig
        S += opn(A[i] @ A[j] @ A[k] @ A[l])
        H += a[i] * a[l] * p[i, j] * p[j, k] * p[k, l]
    assert S * S <= 24 * H * (1 + 1e-9) + 1e-8
print('Hamiltonian aggregate bound passed.')

# DIAGNOSTIC ONLY: conjectured aggregate middle-repeat inequality
#     C23 >= S^2 / (4P).
# No assertion is used: this is not a proof.
min_ratio = float('inf')
for _ in range(1200):
    A = [rand_psd(3, rng) for __ in range(4)]
    S = 0.0
    C23 = 0.0
    P = 0.0
    for i in range(4):
        for j in range(i + 1, 4):
            P += opn(A[i] @ A[j]) ** 2
    for w in itertools.product(range(4), repeat=4):
        cnt = Counter(w)
        shape = sorted(cnt.values(), reverse=True)
        val = opn(A[w[0]] @ A[w[1]] @ A[w[2]] @ A[w[3]])
        if shape == [1, 1, 1, 1]:
            S += val
        elif shape == [2, 1, 1]:
            rep = [z for z, n in cnt.items() if n == 2][0]
            pos = tuple(i for i, z in enumerate(w) if z == rep)
            if pos == (1, 2):
                C23 += val
    if S > 1e-12:
        ratio = 4 * P * C23 / (S * S)
        min_ratio = min(min_ratio, ratio)
print('DIAGNOSTIC ONLY min 4 P C23 / S^2 =', min_ratio)

# Deterministic counterexample to the tempting but false route
#     ||ABC||^2 <= ||A|| ||C|| ||A B^2 C||.
def make_psd_from(seed, d=3):
    rr = np.random.default_rng(seed)
    mats = []
    for _ in range(3):
        Q, _ = np.linalg.qr(rr.normal(size=(d, d)))
        vals = np.exp(rr.uniform(-5, 3, size=d))
        mats.append(Q @ np.diag(vals) @ Q.T)
    return mats


A, B, C = make_psd_from(1557, 3)
lhs = opn(A @ B @ C) ** 2
rhs = opn(A) * opn(C) * opn(A @ B @ B @ C)
print('false-route ratio =', lhs / rhs)
assert lhs > rhs * 1.2

print('All proved-corollary checks passed; the C23 line is diagnostic only.')
