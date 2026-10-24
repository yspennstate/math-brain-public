# Does the best per-coordinate constant equal the global ratio for ARBITRARY Boolean functions?  Same LP as
# ltf_best_assign.py, applied to random truth tables, tribes (disjunctions of disjoint conjunctions) and majorities of
# small odd arity under random product measures.  Reports the largest gap C* - global.
import numpy as np, random, sys, math
from ltf_best_assign import feasible

def spectrum_tt(f, q):
    n = len(q); N = 1 << n
    if min(f) == max(f): return None
    a = np.array([1 - 2 * v for v in f], float)
    for i in range(n):
        s = math.sqrt(q[i] * (1 - q[i])); bit = 1 << i
        for x in range(N):
            if not x & bit:
                f0, f1 = a[x], a[x | bit]
                a[x] = (1 - q[i]) * f0 + q[i] * f1; a[x | bit] = s * (f1 - f0)
    sets = []
    for A in range(1, N):
        k = bin(A).count('1')
        if k < 2: continue
        PA = a[A] ** 2
        if PA <= 1e-300: continue
        sA = 1.0
        for i in range(n):
            if (A >> i) & 1: sA *= 4 * q[i] * (1 - q[i])
        sets.append((A, PA * math.log(sA / PA), k * PA))
    return sets

def best(f, q):
    sets = spectrum_tt(f, q)
    if not sets: return None
    n = len(q)
    glob = sum(e for _, e, _ in sets) / sum(b for _, _, b in sets)
    lo, hi = max(glob, 0.0), max(glob, 0.0) + 1.0
    while not feasible(sets, n, hi): lo, hi = hi, 2 * hi + 1
    for _ in range(30):
        mid = (lo + hi) / 2
        if feasible(sets, n, mid): hi = mid
        else: lo = mid
    return hi, glob

rng = random.Random(int(sys.argv[1])); T = int(sys.argv[2])
gap = (0.0, None)
def rq(n): return [10 ** -rng.uniform(0, 3) if rng.random() < 0.3 else rng.uniform(0.05, 0.95) for _ in range(n)]
for t in range(T):
    kind = t % 3
    if kind == 0:
        n = rng.randint(3, 6); f = [rng.randint(0, 1) for _ in range(1 << n)]; name = 'random'
    elif kind == 1:
        s = rng.randint(2, 3); n = 2 * s
        f = [1 if any((x >> (2 * j)) & 1 and (x >> (2 * j + 1)) & 1 for j in range(s)) else 0 for x in range(1 << n)]; name = 'tribes'
    else:
        n = rng.choice([3, 5]); f = [1 if bin(x).count('1') > n // 2 else 0 for x in range(1 << n)]; name = 'majority'
    q = rq(n)
    r = best(f, q)
    if r is None: continue
    if r[0] - r[1] > gap[0]: gap = (r[0] - r[1], (name, n, ['%.3g' % v for v in q], round(r[0], 4), round(r[1], 4)))
    if t % 30 == 0: print(t, 'largest gap C* - global so far %.2e' % gap[0], gap[1], flush=True)
print('DONE largest gap C* - global = %.3e at %s' % gap)
