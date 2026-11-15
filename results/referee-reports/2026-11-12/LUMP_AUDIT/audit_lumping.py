"""Independent audit of the 12 Nov lumping results (an agent). Route differs from the two earlier rechecks:
tmix is computed from the fundamental matrix, tmix = max_{i,j} -Z_ij / pi_j with Z = (I - P + 1 pi^T)^{-1} - 1 pi^T
(exact Fractions), and cross-checked in floats against direct hitting-time solves.
 A  the four-state family: closed forms for tmix(X) and tmix(quotient), ratio -> 2
 B  the fork comb on 2N+4 states: ratio -> N+2
 C  random search for a violation of each link of  tmix(hX) <= tau0(hX) <= (q-1) tau2(hX) <= (q-1) tau2(X)
    <= (q-1) tmix(X), and of the conclusion tmix(hX) <= (n-2) tmix(X)
"""
import itertools, random, sys
from fractions import Fraction as Fr

import numpy as np


def inv(M):
    n = len(M)
    A = [list(r) + [Fr(int(i == j)) for j in range(n)] for i, r in enumerate(M)]
    for c in range(n):
        p = next(r for r in range(c, n) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        d = A[c][c]
        A[c] = [x / d for x in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return [r[n:] for r in A]


def tmix_exact(W):
    """W: symmetric dict-of-dict / matrix of Fractions, loops counted once in the row sum."""
    n = len(W)
    deg = [sum(W[i]) for i in range(n)]
    tot = sum(deg)
    pi = [d / tot for d in deg]
    M = [[Fr(int(i == j)) - W[i][j] / deg[i] + pi[j] for j in range(n)] for i in range(n)]
    Zi = inv(M)
    return max(-(Zi[i][j] - pi[j]) / pi[j] for i in range(n) for j in range(n))


def quotient(W, blocks):
    q = len(blocks)
    return [[sum(W[i][j] for i in blocks[a] for j in blocks[b]) for b in range(q)] for a in range(q)]


def sym(n, edges):
    W = [[Fr(0)] * n for _ in range(n)]
    for i, j, w in edges:
        W[i][j] += Fr(w)
        if i != j:
            W[j][i] += Fr(w)
    return W


fails = []


def check(ok, what):
    print(("PASS  " if ok else "FAIL  ") + what)
    if not ok:
        fails.append(what)


# A
for t in (2, 3, 7, 10, 100, 10 ** 6):
    t = Fr(t)
    W = sym(4, [(0, 2, 1), (1, 2, 1), (0, 3, t), (1, 3, t), (0, 0, t * t - 1), (1, 1, t * t - 1), (3, 3, t ** 6)])
    Wq = quotient(W, [[0], [1], [2, 3]])
    D = t ** 6 + 2 * t * t + 4 * t + 2
    a, b = tmix_exact(W), tmix_exact(Wq)
    ca, cb = (t + 1) * (t ** 6 + t ** 5 + 4 * t + 2) / D, 2 * t * (t ** 6 + t * t + 3 * t + 2) / D
    check(a == ca and b == cb, "A t=%s closed forms equal; ratio %.12f" % (t, float(b / a)))
check(float(b / a) < 2, "A ratio stays below 2 at t = 10^6 (the factor is approached, not reached)")


# B
def fork(N, t):
    t = Fr(t); r = t ** 3; al = t
    names = ["a", "b", "c"] + ["z%d" % k for k in range(N + 1)] + ["y%d" % k for k in range(N)]
    ix = {s: i for i, s in enumerate(names)}
    E = [("a", "z0", 1), ("b", "z%d" % N, al * r ** (N + 1)), ("c", "z%d" % N, r ** (N + 2)),
         ("a", "a", t - 1), ("b", "b", (t - 1) * al * r ** (N + 1)), ("c", "c", (N + 2) * r ** (N + 4))]
    for k in range(N):
        E += [("z%d" % k, "z%d" % (k + 1), r ** (k + 1)), ("y%d" % k, "z%d" % (k + 1), al * r ** (k + 1)),
              ("y%d" % k, "y%d" % k, (t - 1) * al * r ** (k + 1))]
    W = sym(len(names), [(ix[i], ix[j], w) for i, j, w in E])
    blocks = [[ix["a"]], [ix["b"]]] + [[ix["z%d" % k], ix["y%d" % k]] for k in range(N)] + [[ix["z%d" % N], ix["c"]]]
    return W, blocks


for N in (0, 1, 2, 3):
    W, blocks = fork(N, 1000)
    ratio = tmix_exact(quotient(W, blocks)) / tmix_exact(W)
    W5, b5 = fork(N, 10 ** 5)
    r5 = tmix_exact(quotient(W5, b5)) / tmix_exact(W5)
    # the gap to N+2 should shrink about a hundredfold from t = 10^3 to t = 10^5 and stay positive
    check(ratio < r5 < N + 2 and (N + 2 - r5) < (N + 2 - ratio) / 50,
          "B fork comb N=%d, %d states, %d blocks: ratio %.12f at t=10^3, %.12f at t=10^5 (limit %d)" % (
              N, len(W), len(blocks), float(ratio), float(r5), N + 2))


# C
def stats(W):
    W = np.asarray(W, dtype=float)
    n = len(W)
    deg = W.sum(1); pi = deg / deg.sum()
    P = W / deg[:, None]
    Z = np.linalg.inv(np.eye(n) - P + np.outer(np.ones(n), pi)) - np.outer(np.ones(n), pi)
    tm = (-Z / pi[None, :]).max()
    # direct hitting times, second route
    H = np.zeros((n, n))
    for j in range(n):
        keep = [i for i in range(n) if i != j]
        h = np.linalg.solve(np.eye(n - 1) - P[np.ix_(keep, keep)], np.ones(n - 1))
        H[keep, j] = h
    tm2 = (H - (pi[:, None] * H).sum(0)[None, :]).max()
    S = np.sqrt(pi)[:, None] * P / np.sqrt(pi)[None, :]
    ev = np.sort(np.linalg.eigvalsh((S + S.T) / 2))[::-1]
    tau2 = 1.0 / (1.0 - ev[1])
    tau0 = float(np.sum(1.0 / (1.0 - ev[1:])))
    return tm, tm2, tau0, tau2


def partitions(n):
    def rec(i, blocks):
        if i == n:
            yield [list(b) for b in blocks]
            return
        for b in blocks:
            b.append(i); yield from rec(i + 1, blocks); b.pop()
        blocks.append([i]); yield from rec(i + 1, blocks); blocks.pop()
    yield from rec(0, [])


rng = random.Random(20261112)
worst = {}
viol = {k: 0 for k in ("tmix<=tau0", "tau0<=(q-1)tau2", "tau2(q)<=tau2(X)", "tau2<=tmix", "conclusion", "two routes agree")}
trials = 0
big = {}
for trial in range(6000):
    n = rng.choice((3, 4, 4, 5, 5, 6))
    while True:
        W = np.zeros((n, n))
        dens = rng.uniform(0.3, 1.0)
        for i in range(n):
            for j in range(i, n):
                if rng.random() < dens:
                    W[i, j] = W[j, i] = 10 ** rng.uniform(-3, 3)
        # connected and not bipartite-degenerate enough for the solves
        A = (W > 0).astype(float) + np.eye(n)
        if (np.linalg.matrix_power(A, n) > 0).all():
            break
    tm, tm2, tau0, tau2 = stats(W)
    if abs(tm - tm2) > 1e-6 * max(1.0, tm):
        viol["two routes agree"] += 1
    if tau2 > tm * (1 + 1e-7):
        viol["tau2<=tmix"] += 1
    if tm > tau0 * (1 + 1e-7):
        viol["tmix<=tau0"] += 1
    parts = [p for p in partitions(n) if 2 <= len(p) <= n - 1]
    for blocks in rng.sample(parts, min(len(parts), 6)):
        trials += 1
        q = len(blocks)
        Wq = np.array([[W[np.ix_(a, b)].sum() for b in blocks] for a in blocks])
        tq, tq2, t0q, t2q = stats(Wq)
        if t0q > (q - 1) * t2q * (1 + 1e-7):
            viol["tau0<=(q-1)tau2"] += 1
        if t2q > tau2 * (1 + 1e-7):
            viol["tau2(q)<=tau2(X)"] += 1
        if tq > max(1, n - 2) * tm * (1 + 1e-7):
            viol["conclusion"] += 1
        if tm > 1e-12:
            big[n] = max(big.get(n, 0.0), tq / tm)
print("C %d chains, %d (chain, partition) pairs; violations %s" % (6000, trials, viol))
print("C largest ratio seen by random search, by n: %s" % {k: round(v, 4) for k, v in sorted(big.items())})
check(all(v == 0 for v in viol.values()), "C no violation of any link or of the conclusion")
print("--- %d failed" % len(fails))
sys.exit(1 if fails else 0)
