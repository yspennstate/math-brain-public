"""Independent check of FEIB09's fixed-level containment bounds, and a first look at the increments.

A_r(f) = sum_S mu(S) max_{R subset S, |R| <= r} log2(1/up(R))      (A_n = A)
G_r(f) = the same along the greedy chain R_1 < R_2 < ... (add the element that minimises up), G_r <= A_r, G_n = A.
Claims checked: A_1 <= 3.520226 I; A_r <= r A_1 + I/ln 2; A_2 <= 6.1033 I; A_3 <= 7.872677 I.
Looked at: sup A_r/I, and sup r (A_r - A_{r-1}) / I, sup r (G_r - G_{r-1}) / I (is the increment O(I/r)?).
Usage: python check_feib09.py 4            all functions on 4 variables
       python check_feib09.py 6 20000 7    20000 random functions on 6 variables, seed 7 (three biases)
"""
import sys
import numpy as np

n = int(sys.argv[1])
N = 1 << n
LN2 = np.log(2.0)


def wht(a):
    a = a.copy()
    h = 1
    while h < N:
        a = a.reshape(-1, N // (2 * h), 2, h)
        x = a[:, :, 0, :] + a[:, :, 1, :]
        y = a[:, :, 0, :] - a[:, :, 1, :]
        a = np.stack([x, y], axis=2).reshape(-1, N)
        h *= 2
    return a / N


def tables():
    if len(sys.argv) == 2:
        idx = np.arange(1 << N, dtype=np.uint64)
        bits = ((idx[:, None] >> np.arange(N, dtype=np.uint64)[None, :]) & 1).astype(np.float64)
        yield 1.0 - 2.0 * bits
    else:
        cnt, seed = int(sys.argv[2]), int(sys.argv[3])
        rng = np.random.default_rng(seed)
        for bias in (0.5, 0.25, 0.1):
            yield 1.0 - 2.0 * (rng.random((cnt, N)) < bias)
        # structured: AND_n, OR of two ANDs, majority (n odd) or majority with tie -> x1
        x = 1 - 2 * ((np.arange(N)[:, None] >> np.arange(n)[None, :]) & 1)   # +-1 inputs, rows = points
        f_and = np.where((x == 1).all(axis=1), -1.0, 1.0)
        s = x.sum(axis=1)
        f_maj = np.where(s > 0, 1.0, np.where(s < 0, -1.0, x[:, 0].astype(float)))
        h = n // 2
        f_tr = np.where((x[:, :h] == 1).all(axis=1) | (x[:, h:] == 1).all(axis=1), -1.0, 1.0)
        yield np.stack([f_and, f_maj, f_tr])


pop = np.array([bin(s).count("1") for s in range(N)])
subs = [[r for r in range(N) if r & ~s == 0] for s in range(N)]
worst = {}


def upd(key, val, tt):
    j = int(np.nanargmax(val))
    if key not in worst or val[j] > worst[key][0]:
        worst[key] = (float(val[j]), tt[j].copy())


total = 0
for f in tables():
    fh = wht(f)
    mu = fh * fh
    up = np.zeros_like(mu)
    for s in range(N):
        up[:, s] = mu[:, [u for u in range(N) if u & s == s]].sum(axis=1)
    with np.errstate(divide="ignore"):
        cost = np.where(up > 0, -np.log2(np.maximum(up, 1e-300)), 0.0)      # log2(1/up(R)); only used where mu(S) > 0
    I = (mu * pop[None, :]).sum(axis=1)
    A = np.zeros((f.shape[0], n + 1))
    G = np.zeros((f.shape[0], n + 1))
    for s in range(1, N):
        m = mu[:, s]
        for r in range(1, n + 1):
            rs = [q for q in subs[s] if 0 < pop[q] <= r]
            A[:, r] += m * cost[:, rs].max(axis=1)
        # greedy chain inside s
        cur = np.zeros(f.shape[0], dtype=np.int64)
        els = [i for i in range(n) if s >> i & 1]
        for r in range(1, n + 1):
            if r <= len(els):
                cand = np.stack([np.where((cur >> i) & 1, -1.0, cost[np.arange(f.shape[0]), cur | (1 << i)])
                                 for i in els], axis=1)
                pick = np.array(els)[cand.argmax(axis=1)]
                cur = cur | (1 << pick)
            G[:, r] += m * cost[np.arange(f.shape[0]), cur]
    ok = I > 1e-12
    Is = np.where(ok, I, np.nan)
    assert np.all(np.abs(A[:, n] - G[:, n]) < 1e-9), "greedy chain must end at S"
    c1 = 3.520226
    v = [np.nanmax(A[:, 1] - c1 * I), np.nanmax(A[:, 2] - 6.1033 * I) if n >= 2 else 0,
         np.nanmax(A[:, 3] - 7.872677 * I) if n >= 3 else 0,
         max(np.nanmax(A[:, r] - r * A[:, 1] - I / LN2) for r in range(1, n + 1))]
    assert max(v) < 1e-9, ("VIOLATION", v)
    for r in range(1, n + 1):
        upd("A_%d/I" % r, A[:, r] / Is, f)
        upd("G_%d/I" % r, G[:, r] / Is, f)
        if r >= 2:
            upd("r(A_r-A_r-1)/I r=%d" % r, r * (A[:, r] - A[:, r - 1]) / Is, f)
            upd("r(G_r-G_r-1)/I r=%d" % r, r * (G[:, r] - G[:, r - 1]) / Is, f)
    total += f.shape[0]

print("n =", n, "functions checked:", total, " all four FEIB09 bounds hold (tolerance 1e-9)")
for k in sorted(worst):
    val, tt = worst[k]
    hx = "%0*x" % (N // 4, int("".join("1" if t < 0 else "0" for t in tt[::-1]), 2))
    print("  sup %-24s %.6f   tt 0x%s" % (k, val, hx))
