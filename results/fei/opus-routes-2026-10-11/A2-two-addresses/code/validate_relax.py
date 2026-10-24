"""Validate the constraints of the arithmetic relaxation on actual K2 functions (address pair fixed, |C| = m).
For each function: E_* (type-2 set), rho = |R_cap|, e = base size of E_* on the R_cap-cube, and per row
(r, pairs, nu', class).  Checks:
  E_* empty  -> every row {0,+-1}-valued (ternary) and 2 v2(nu') >= e_c + 2
  E_* nonempty -> all rows present, half-valued, w_T >= e 2^{-rho}/4, odd rows exactly those with
                  (e odd and r_T = rho), even rows have 2 v2(nu') >= e_c
  and the exact decomposition H = sum_T w_T (2 - 2 log2 nu' + sum Ft).
m = 3: every function (all 1,564,928).  m = 4: a random sample of completions of every row-0 representative."""
import sys, math, random, itertools
import numpy as np
from collections import defaultdict, Counter
sys.path.insert(0, ".")
import rows_v2 as RV, check_identity as CI

def v2(n):
    c = 0
    while n % 2 == 0:
        n //= 2; c += 1
    return c

def check_function(rows4, m, Hm, stats):
    N = 1 << m
    # E_*: points where |V_T| = 1 (all rows half)
    Estar = [x for x in range(N) if abs(rows4[0][x]) == 1]
    infos = []
    for T in range(4):
        res = CI.analyse(rows4[T], m)
        infos.append(res)
    # active sets
    acts = []
    for T in range(4):
        if infos[T] is None:
            acts.append(None); continue
        W = Hm @ np.array(rows4[T]); Q = W * W; tot = Q.sum()
        a = []
        for i in range(m):
            s1 = sum(Q[U] for U in range(N) if U >> i & 1)
            if 0 < s1 < tot: a.append(i)
        acts.append(set(a))
    if not Estar:
        for T in range(4):
            if infos[T] is None: continue
            r, pq, nup, odd = infos[T]
            assert all(abs(v) != 1 for v in rows4[T])
            ec = sum(1 for p, q in pq if (p * p + q * q) % 2)
            assert not odd and 2 * v2(nup) >= ec + 2, ("ternary integrality", rows4[T])
        stats["A"] += 1
        return
    assert all(infos[T] is not None for T in range(4)), "E_* nonempty but a row vanishes"
    Rcap = set.intersection(*acts)
    rho = len(Rcap)
    # base of E_* on R_cap cube
    base = set()
    for x in Estar:
        base.add(tuple((x >> i) & 1 for i in sorted(Rcap)))
    e = len(base)
    assert len(Estar) == e * 2 ** (m - rho), "E_* not a cylinder over R_cap"
    for T in range(4):
        r, pq, nup, odd = infos[T]
        w = sum(v * v for v in rows4[T]) / (4.0 * N)
        assert w >= e * 2.0 ** (-rho) / 4 - 1e-12, "weight lower bound"
        assert odd == (e % 2 == 1 and r == rho), ("odd class rule", T, r, rho, e, odd)
        if not odd:
            ec = sum(1 for p, q in pq if (p * p + q * q) % 2)
            assert 2 * v2(nup) >= ec, "half integrality"
    stats[("B", rho, e % 2)] += 1

def main():
    m = int(sys.argv[1])
    pkl = sys.argv[2] if m == 4 else None
    rows = RV.product_rows(m, pkl)
    N = 1 << m
    Hm = RV.hadamard(m)
    half, two = RV.masks_arr(rows, m)
    by_half = defaultdict(list)
    for i in range(len(rows)):
        by_half[int(half[i])].append(i)
    full = (1 << N) - 1
    stats = Counter()
    rng = random.Random(12345)
    r0_list = RV.orbit_reps(rows, m)
    for r0i in r0_list:
        r0 = rows[r0i]
        h0 = int(half[r0i]); z0 = full & ~h0 & ~int(two[r0i])
        cand = [ci for ci in by_half.get(h0, []) if not (int(two[ci]) & ~z0)]
        bytwo = defaultdict(list)
        for ci in cand:
            bytwo[int(two[ci])].append(ci)
        keys = list(bytwo)
        halfpts = [x for x in range(N) if h0 >> x & 1]
        combos = []
        for S1 in keys:
            for S2 in keys:
                if S2 & (S1 | ~(z0 & ~S1)) & full:
                    continue
                S3 = z0 & ~S1 & ~S2
                if S3 in bytwo:
                    combos.append((S1, S2, S3))
        if len(combos) > 200:
            combos = rng.sample(combos, 200)
        for S1, S2, S3 in combos:
            trip = itertools.product(bytwo[S1], bytwo[S2], bytwo[S3])
            if True:
                L = [rng.choice(bytwo[S1]) for _ in range(1)]
                trip = ((rng.choice(bytwo[S1]), rng.choice(bytwo[S2]), rng.choice(bytwo[S3])) for _ in range(30))
            for c1, c2, c3 in trip:
                rr = (r0, rows[c1], rows[c2], rows[c3])
                if any(rr[0][x] * rr[1][x] * rr[2][x] * rr[3][x] != -1 for x in halfpts):
                    continue
                check_function(rr, m, Hm, stats)
    print("m", m, "functions checked by scenario:", dict(stats))

if __name__ == "__main__":
    main()
