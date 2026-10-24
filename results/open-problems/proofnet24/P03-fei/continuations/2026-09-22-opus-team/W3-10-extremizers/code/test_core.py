import numpy as np, itertools, sys
sys.path.insert(0, '.')
from core import *
polite()
AND3 = tt_from_pred(3, lambda b: b.all())
MAJ3 = tt_from_pred(3, lambda b: b.sum() >= 2)
MUX = tt_from_pred(3, lambda b: b[1] if b[0] else b[2])
XOR3 = tt_from_pred(3, lambda b: b.sum() % 2 == 1)
for nm, t in [("AND3", AND3), ("MAJ3", MAJ3), ("MUX", MUX), ("XOR3", XOR3)]:
    s = stats(t)
    print(nm, decompose(t), "prime=", is_prime(t), "H=%.6f I=%.6f rho0=%.6f" % (s['H'], s['I'], s['rho0']))
# NPN classes at n=3,4 and prime counts
def npn_canon_all(n):
    N = 1 << n
    x = np.arange(N)
    maps = []
    for perm in itertools.permutations(range(n)):
        for neg in range(N):
            # y = transform of x: bit perm[i] of y = bit i of x xor neg bit i
            y = np.zeros(N, dtype=np.int64)
            for i in range(n):
                y |= (((x >> i) & 1) ^ ((neg >> i) & 1)) << perm[i]
            maps.append(y)
    maps = np.array(maps)
    return maps
for n in (3, 4):
    N = 1 << n
    maps = npn_canon_all(n)
    allf = ((np.arange(1 << N)[:, None] >> np.arange(N)[None, :]) & 1).astype(np.int64)  # bit=1 -> true
    pw = (1 << np.arange(N)).astype(np.int64)
    best = None
    for y in maps:
        # g(y(x)) = f(x)  -> table of g: g[y[x]] = f[x]
        g = np.empty_like(allf); g[:, y] = allf
        for neg_out in (0, 1):
            code = ((g ^ neg_out) * pw).sum(axis=1)
            best = code if best is None else np.minimum(best, code)
    reps = np.unique(best)
    full = 0; prime = 0
    for c in reps:
        t = np.array([(-1 if (c >> k) & 1 else 1) for k in range(N)], dtype=np.int8)
        if len(relevant(t)) == n:
            full += 1
            if is_prime(t): prime += 1
    print("n=%d NPN classes %d, full-support %d, prime %d" % (n, len(reps), full, prime))
    np.save("../logs/npn_reps_n%d.npy" % n, reps)
