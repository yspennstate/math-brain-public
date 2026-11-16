"""Independent numerical check of op1_exact.py (Mossel-O'Donnell Open Problem 1).
n=7: the antisymmetric left-monotone functions are found by filtering all 1,422,564 self-dual monotone
functions (different code from the backtracking in op1_exact.py); n=8: a fresh backtracking over pairs.
Then P_k(f; e) = 2^{-n} sum_x [p^k + (1-p)^k] in float64 on 4000 values of e in (0, 1/2), k = 2..9,
compared with the dictator on the first coordinate.  Usage: python num_check.py n
"""
import sys, time
import numpy as np

n = int(sys.argv[1]); N = 1 << n
t0 = time.time()
# variable j <-> bit j of the table index; "left" order: prefix sums over variables 0, 1, ..., n-1
X = ((np.arange(N)[:, None] >> np.arange(n)) & 1)
covers = []                       # pairs (x, y) with y covering x in <=_L: set a 0 to 1, or move a 1 left
for x in range(N):
    for j in range(n):
        if not X[x, j]:
            covers.append((x, x | (1 << j)))
        if j + 1 < n and X[x, j + 1] and not X[x, j]:
            covers.append((x, x ^ (1 << j) ^ (1 << (j + 1))))
cx = np.array([c[0] for c in covers]); cy = np.array([c[1] for c in covers])

if n == 7:
    sys.path.insert(0, '.')
    def monotone(m):
        fs = np.array([0, 1], dtype=np.uint64)
        for k in range(m):
            sh = np.uint64(1 << k)
            fs = np.concatenate([a | (fs[(a & ~fs) == 0] << sh) for a in fs])
        return fs
    REV8 = np.array([int(f'{b:08b}'[::-1], 2) for b in range(256)], dtype=np.uint8)
    def rev64(a):
        b = a.astype('<u8').view(np.uint8).reshape(-1, 8)
        return REV8[b][:, ::-1].copy().view('<u8').ravel().astype(np.uint64)
    H = monotone(6)
    Dm = rev64(H) ^ np.uint64(0xFFFFFFFFFFFFFFFF)
    keep = (Dm & ~H) == 0
    H, Dm = H[keep], Dm[keep]
    assert len(H) == 1422564
    tabs = []
    for s in range(0, len(H), 50000):
        lo = ((Dm[s:s + 50000, None] >> np.arange(64, dtype=np.uint64)) & np.uint64(1)).astype(np.int8)
        hi = ((H[s:s + 50000, None] >> np.arange(64, dtype=np.uint64)) & np.uint64(1)).astype(np.int8)
        F = np.concatenate([lo, hi], axis=1)
        ok = ~((F[:, cx] == 1) & (F[:, cy] == 0)).any(1)
        tabs.append(F[ok])
    T = np.concatenate(tabs)
else:
    comp = lambda x: (N - 1) ^ x
    succ = [[] for _ in range(N)]; pred = [[] for _ in range(N)]
    for a, b in covers:
        succ[a].append(b); pred[b].append(a)
    res = []
    val = [-1] * N
    def setv(x, v, stack):
        if val[x] == v:
            return True
        if val[x] != -1:
            return False
        val[x] = v; stack.append(x)
        nxt = succ[x] if v == 1 else pred[x]
        return all(setv(y, v, stack) for y in nxt) and setv(comp(x), 1 - v, stack)
    sys.setrecursionlimit(100000)
    def rec(i):
        while i < N and val[i] != -1:
            i += 1
        if i == N:
            res.append(list(val)); return
        for v in (0, 1):
            st = []
            if setv(i, v, st):
                rec(i + 1)
            for x in st:
                val[x] = -1
    rec(0)
    T = np.array(res, dtype=np.int8)
assert not ((T[:, cx] == 1) & (T[:, cy] == 0)).any()
assert (T[:, ::-1] + T == 1).all()            # antisymmetric: f(~x) = 1 - f(x); ~x is index N-1-x
print(f"n={n}: {len(T)} antisymmetric left-monotone functions ({time.time()-t0:.0f}s)", flush=True)

dict1 = X[:, 0].astype(np.int8)
assert any((T == dict1).all(1))
d = (X[:, None, :] != X[None, :, :]).sum(-1)
es = np.linspace(0, 0.5, 4002)[1:-1]
worst = {}
for k in range(2, 10):
    mn = np.inf; arg = None
    for e in es:
        K = e ** d * (1 - e) ** (n - d)
        P = T.astype(float) @ K.T                  # p(x) for each f
        A = (P ** k + (1 - P) ** k).mean(1)
        p1 = dict1 @ K.T
        a1 = (p1 ** k + (1 - p1) ** k).mean()
        D = (a1 - A) / (e * (1 - 2 * e) ** 2)      # the difference vanishes like e at 0 and (1-2e)^2 at 1/2
        assert np.isfinite(D).all() and np.isfinite(a1), (k, e)
        D[(T == dict1).all(1)] = np.inf
        j = int(D.argmin())
        if D[j] < mn:
            mn, arg = D[j], (round(float(e), 5), j)
    worst[k] = (float(mn), arg)
    print(f"k={k}: min over f,e of (P_k(x1)-P_k(f))/(e(1-2e)^2) = {mn:.3e} at e,f={arg}", flush=True)
print("ALL POSITIVE" if all(v[0] > 0 for v in worst.values()) else "SOME NONPOSITIVE", f"({time.time()-t0:.0f}s)")
