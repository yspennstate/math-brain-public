# The best per-coordinate constant over ALL assignments.  Each set A (|A| >= 2) is divided among its elements
# (x_{A,j} >= 0, sum_j x_{A,j} = 1); coordinate j is charged sum_A x_{A,j} e_A with e_A = P(A) ln(sigma_A^2/P(A)) against
# the budget sum_A x_{A,j} b_A with b_A = |A| P(A).  A constant C is achievable iff the linear programme
#     sum_A x_{A,j} (e_A - C b_A) <= 0 for every j
# is feasible; by LP duality this is a Hall-type condition over subsets U of coordinates, whose U = everything case is
# the global inequality sum e_A <= C J.  C* = the least achievable constant, found by bisection.  If C* stays bounded
# for linear threshold functions, a per-coordinate proof is possible in principle and only the assignment rule is
# missing.  Moderate biases only (float LP).
import numpy as np, random, sys, math
from scipy.optimize import linprog

def spectrum(w, theta, q):
    n = len(w); N = 1 << n
    f = np.array([1 if sum(w[i] for i in range(n) if (x >> i) & 1) >= theta else 0 for x in range(N)], float)
    if f.min() == f.max(): return None
    a = 1 - 2 * f
    for i in range(n):
        s = math.sqrt(q[i] * (1 - q[i])); bit = 1 << i
        a = a.copy()
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

def feasible(sets, n, C):
    # variables: one per (set, member); equality per set; inequality per coordinate
    var = []
    for si, (A, e, b) in enumerate(sets):
        for j in range(n):
            if (A >> j) & 1: var.append((si, j))
    nv = len(var)
    J = sum(b for _, _, b in sets)
    A_eq = np.zeros((len(sets), nv)); b_eq = np.ones(len(sets))
    A_ub = np.zeros((n, nv)); b_ub = np.zeros(n)
    for v, (si, j) in enumerate(var):
        A_eq[si, v] = 1
        e, b = sets[si][1], sets[si][2]
        A_ub[j, v] = (e - C * b) / J
    res = linprog(np.zeros(nv), A_ub=A_ub, b_ub=b_ub + 1e-12, A_eq=A_eq, b_eq=b_eq, bounds=(0, None), method='highs')
    return res.status == 0

def best_C(w, theta, q):
    sets = spectrum(w, theta, q)
    if not sets: return None
    n = len(w)
    glob = sum(e for _, e, _ in sets) / sum(b for _, _, b in sets)
    lo, hi = max(glob, 0.0), max(glob, 0.0) + 1.0
    while not feasible(sets, n, hi): lo, hi = hi, 2 * hi + 1
    for _ in range(30):
        mid = (lo + hi) / 2
        if feasible(sets, n, mid): hi = mid
        else: lo = mid
    return hi, glob

if __name__ == '__main__':
    rng = random.Random(int(sys.argv[1])); T = int(sys.argv[2]); nmax = int(sys.argv[3])
    for m in [4, 6]:
        r = best_C([float(m)] + [1.0] * m, m / 2, [0.5] * (m + 1))
        print('heavy-plus-light m', m, 'C* %.4f  global %.4f' % r, flush=True)
    r = best_C([4.0, 1.0, 1.0, 8.0, 2.0, 2.0], 17.593, [8.07e-5, 1e-4, 1e-4, 0.00853, 1e-4, 0.895])
    print('lightest-owner failure instance (biases floored at 1e-4): C* %.4f  global %.4f' % r, flush=True)
    worst = (0.0, None); gap = (0.0, None); cnt = 0
    for t in range(T):
        n = rng.randint(3, nmax)
        kind = rng.random()
        if kind < 0.2: w = [1.0] * n
        elif kind < 0.4: w = [float(rng.randint(1, 3)) for _ in range(n)]
        elif kind < 0.6: w = [2.0 ** rng.randint(0, 5) for _ in range(n)]
        elif kind < 0.8: w = [rng.expovariate(1.0) + 0.01 for _ in range(n)]
        else: w = [float(n)] + [1.0] * (n - 1)
        theta = rng.uniform(0.001, sum(w))
        q = [10 ** -rng.uniform(0, 4) if rng.random() < 0.3 else (1 - 10 ** -rng.uniform(0, 4) if rng.random() < 0.4 else rng.uniform(0.02, 0.98)) for _ in range(n)]
        r = best_C(w, theta, q)
        if r is None: continue
        cnt += 1
        if r[0] > worst[0]: worst = (r[0], (n, [round(v, 3) for v in w], round(theta, 3), ['%.3g' % x for x in q], round(r[1], 4)))
        if r[0] - r[1] > gap[0]: gap = (r[0] - r[1], (n, [round(v, 3) for v in w], round(theta, 3), ['%.3g' % x for x in q], round(r[0], 4), round(r[1], 4)))
        if t % 50 == 0: print(t, 'max C* so far %.4f  largest gap C* - global %.2e' % (worst[0], gap[0]), flush=True)
    print('DONE %d instances; max C* = %.4f at %s (last field: the global ratio of that instance)' % (cnt, worst[0], worst[1]))
    print('DONE largest gap C* - global over all instances = %.3e at %s' % gap)
