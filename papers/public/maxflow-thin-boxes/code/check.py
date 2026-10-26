"""Checks for "Maximal flow through thin boxes with heavy-tailed capacities".

Part 1 (exact, fractions): the law of Example 1.3, its tails, the column probability,
the Chebyshev bound and the final lower bound, for r = 1..12.
Part 2 (exact, integers): max-flow/min-cut on small random boxes; every computed maximal
flow is at least a * (number of columns whose edges all have capacity >= a).

Run: python check.py   (needs numpy and scipy). Writes nothing; the output is check_output.txt.
"""
from fractions import Fraction as Fr
import math

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_flow

ok = True


def report(name, cond):
    global ok
    ok = ok and bool(cond)
    print(("PASS " if cond else "FAIL ") + name)


# ---------------------------------------------------------------- part 1
# Example 1.3: N_r = 2^(4 r^2), a_r = N_r, P(T=1) = 1/2, P(T=a_s) = 2^(-s-1).
R = 12
N = [None] + [2 ** (4 * r * r) for r in range(1, R + 1)]


def m_height(n):  # m(k, l) = max(1, floor(sqrt(log2 min(k, l)))) on the diagonal
    return max(1, math.isqrt(n.bit_length() - 1)) if n >= 2 else 1


# masses: 1/2 + sum_{s>=1} 2^(-s-1) = 1; partial sums leave exactly 2^(-S-1)
for S in (1, 5, 40):
    part = Fr(1, 2) + sum(Fr(1, 2 ** (s + 1)) for s in range(1, S + 1))
    report(f"mass after {S} atoms leaves exactly 2^-{S+1}", 1 - part == Fr(1, 2 ** (S + 1)))

for r in range(1, R + 1):
    n = N[r]
    m = m_height(n)
    # exact log2 of a power of two, so the integer square root is exact
    report(f"r={r}: m(N_r,N_r) = 2r", m == 2 * r)
    report(f"r={r}: 4^(r m) <= N_r", 4 ** (r * m) <= n)
    report(f"r={r}: N_r >= 2^r and N_r > N_(r-1)", n >= 2 ** r and (r == 1 or n > N[r - 1]))
    # tail P(T >= a_r) = sum_{s>=r} 2^(-s-1) = 2^(-r): partial sum to s = r+60 leaves 2^-(r+61)
    tail = sum(Fr(1, 2 ** (s + 1)) for s in range(r, r + 61))
    report(f"r={r}: P(T >= a_r) = 2^-r (truncation exact)", Fr(1, 2 ** r) - tail == Fr(1, 2 ** (r + 61)))
    pi = Fr(1, 2 ** (r * m))  # column probability
    report(f"r={r}: pi_r = N_r^(-1/2)", pi * pi * n == 1)
    for d in (2, 3):
        mu = (n + 1) ** (d - 1) * pi
        cheb = 4 / mu
        report(f"r={r}, d={d}: 4/mu_r <= 4 * 2^(-2 r^2)", cheb <= Fr(4, 2 ** (2 * r * r)))
        # on {Y >= mu/2}: Phi / N^(d-1) >= a mu / (2 N^(d-1)) >= N^(1/2) / 2
        lower = Fr(n) * mu / (2 * Fr(n) ** (d - 1))
        report(f"r={r}, d={d}: a_r mu_r / (2 N_r^(d-1)) >= 2^(2r^2-1)", lower >= Fr(2 ** (2 * r * r), 2))

# sum of the Chebyshev bounds over r is finite (geometric domination by 4 * 2^(-2r))
report("sum_r 4*2^(-2 r^2) <= 4/3", sum(Fr(4, 2 ** (2 * r * r)) for r in range(1, R + 1)) <= Fr(4, 3))

# infinite mean: partial sums of a_s P(T=a_s) exceed S/2
for S in (4, 8):
    report(f"sum_(s<={S}) a_s 2^(-s-1) >= S/2", sum(Fr(N[s], 2 ** (s + 1)) for s in range(1, S + 1)) >= Fr(S, 2))


# ---------------------------------------------------------------- part 2
def box_maxflow(n, m, cap):
    """Max flow from the bottom face to the top face of {0..n}^2 x {0..m}.

    cap maps each undirected edge (u, v) (u < v in index order) to an integer capacity.
    A super source joins the bottom face and a super sink the top face with infinite capacity."""
    def idx(x, y, z):
        return (z * (n + 1) + y) * (n + 1) + x

    V = (n + 1) ** 2 * (m + 1)
    s, t = V, V + 1
    big = 10 ** 6  # scipy maximum_flow works in int32; this exceeds every cut here
    rows, cols, vals = [], [], []
    for (u, v), c in cap.items():
        rows += [u, v]
        cols += [v, u]
        vals += [c, c]
    for x in range(n + 1):
        for y in range(n + 1):
            rows += [s, idx(x, y, m)]
            cols += [idx(x, y, 0), t]
            vals += [big, big]
    G = csr_matrix((np.array(vals, dtype=np.int32), (rows, cols)), shape=(V + 2, V + 2))
    return maximum_flow(G, s, t).flow_value, idx


rng = np.random.default_rng(20261025)
worst = None
trials = 0
for trial in range(300):
    n = int(rng.integers(1, 5))
    m = int(rng.integers(1, 4))
    a = int(rng.integers(5, 50))
    p_high = float(rng.choice([0.3, 0.6, 0.9]))

    def idx(x, y, z):
        return (z * (n + 1) + y) * (n + 1) + x

    cap = {}
    for z in range(m + 1):
        for y in range(n + 1):
            for x in range(n + 1):
                u = idx(x, y, z)
                for dx, dy, dz in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
                    X, Y, Z = x + dx, y + dy, z + dz
                    if X <= n and Y <= n and Z <= m:
                        hi = rng.random() < p_high
                        cap[(u, idx(X, Y, Z))] = int(rng.integers(a, 3 * a)) if hi else int(rng.integers(1, a))
    phi, _ = box_maxflow(n, m, cap)
    high = sum(
        all(cap[(idx(x, y, z), idx(x, y, z + 1))] >= a for z in range(m))
        for x in range(n + 1) for y in range(n + 1)
    )
    trials += 1
    gap = phi - a * high
    worst = gap if worst is None else min(worst, gap)
    if gap < 0:
        report(f"trial {trial}: Phi >= a * #high columns", False)
report(f"{trials} random boxes: Phi >= a * #high columns (smallest Phi - a*Y = {worst})", worst is not None and worst >= 0)

# a deterministic control: every vertical edge = a, every other edge = 1, so the
# columns carry a each and the minimum cut is a horizontal layer of (n+1)^2 vertical edges
n, m, a = 3, 2, 7
def idx(x, y, z):
    return (z * (n + 1) + y) * (n + 1) + x
cap = {}
for z in range(m + 1):
    for y in range(n + 1):
        for x in range(n + 1):
            for dx, dy, dz in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
                X, Y, Z = x + dx, y + dy, z + dz
                if X <= n and Y <= n and Z <= m:
                    cap[(idx(x, y, z), idx(X, Y, Z))] = a if dz else 1
phi, _ = box_maxflow(n, m, cap)
report(f"control box 3x3x2, vertical capacity 7: Phi = 7*16 = 112 (got {phi})", phi == a * (n + 1) ** 2)

print("RESULT", "PASS" if ok else "FAIL")
