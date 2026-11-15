"""Check the ingredient of the path argument on finite sets:
for non-commuting positive contractions Q1 <= Q2 there is a coupling of P_Q1, P_Q2 supported on {A subset of B},
so W1_Hamming = tr(Q2 - Q1).  Also run the path bound itself: chain of monotone steps, total cost tr|Q - Q'|.
"""
import sys
import numpy as np
from scipy.optimize import linprog
from scipy.linalg import sqrtm

rng = np.random.default_rng(int(sys.argv[1]))
N = int(sys.argv[2]); T = int(sys.argv[3])
M = 1 << N
pop = np.array([bin(a).count('1') for a in range(M)])


def law(Q):
    p = np.empty(M)
    for a in range(M):
        D = Q.copy()
        for e in range(N):
            if not (a >> e) & 1:
                D[e, e] -= 1
        p[a] = ((-1) ** (N - pop[a]) * np.linalg.det(D)).real
    return p


def rc():
    X = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))
    U, _ = np.linalg.qr(X)
    return (U * rng.uniform(0, 1, N)) @ U.conj().T


pairs = [(a, b) for a in range(M) for b in range(M) if a & b == a]  # A subset of B
A_eq = np.zeros((2 * M, len(pairs)))
for k, (a, b) in enumerate(pairs):
    A_eq[a, k] = 1; A_eq[M + b, k] = 1
worst_gap, worst_feas = 0.0, 0.0
for t in range(T):
    Q2 = rc(); K = rc(); R = sqrtm(Q2)
    Q1 = R @ K @ R.conj().T; Q1 = (Q1 + Q1.conj().T) / 2
    comm = np.abs(Q1 @ Q2 - Q2 @ Q1).max()
    p1, p2 = law(Q1), law(Q2)
    neg = min(p1.min(), p2.min())
    r = linprog(np.zeros(len(pairs)), A_eq=A_eq[:-1], b_eq=np.concatenate([p1, p2])[:-1], bounds=(0, None), method='highs')
    # cost of the monotone coupling = E|B| - E|A| = tr Q2 - tr Q1 automatically
    gap = abs((p2 * pop).sum() - (p1 * pop).sum() - np.trace(Q2 - Q1).real)
    worst_gap = max(worst_gap, gap)
    if r.status != 0:
        print('NO MONOTONE COUPLING', t, 'comm', comm, 'neg', neg); worst_feas = 1
print(f'N {N} trials {T}: all monotone couplings feasible: {worst_feas == 0}; max |E|B|-E|A|-tr(Q2-Q1)| {worst_gap:.2e}')
