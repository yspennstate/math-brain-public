"""Exact checks of the row identity on every product row with values in {0,+-1/2,+-1} (stored as V = 2g):

  For a product row g (weight w > 0) with active set R (r = |R|), minimal nonzero coefficient
  kappa = nu * 2^{-r-1} (nu a positive integer), coordinate ratios k_i = p_i/q_i >= 1 in lowest terms:
    (a) prod_i q_i divides nu; nu' = nu / prod q_i is an integer >= 1
    (b) w = nu'^2 4^{-r-1} prod_i (p_i^2 + q_i^2)                       [exact rational check]
    (c) log2(1/w) + H(q) = 2 - 2 log2 nu' + sum_i Ft(p_i, q_i),
        Ft(p,q) = 2 - log2(p^2+q^2) + h(q^2/(p^2+q^2))                   [float check, 1e-9]
    (d) even class (all coefficients in 2^{-r} Z) => nu' even; odd class => nu' odd and every p_i, q_i odd
    (e) odd class <=> the number of points of the R-cube where |g| = 1/2 is odd
Also tabulates the (p,q) pairs and nu' values that occur."""
import numpy as np, math, sys, itertools
from fractions import Fraction
from math import gcd
from collections import Counter
sys.path.insert(0, ".")
import rows_v2 as RV

def h(t):
    return 0.0 if t <= 0 or t >= 1 else -t * math.log2(t) - (1 - t) * math.log2(1 - t)

def Ft(p, q):
    s = p * p + q * q
    return 2 - math.log2(s) + h(q * q / s)

def analyse(row, m):
    N = 1 << m
    Hm = RV.hadamard(m)
    V = np.array(row, dtype=np.int64)
    W = Hm @ V                     # ghat(U) = W(U) / (2N);  2^{m+1} ghat = W
    Q = W * W
    tot = int(Q.sum())
    if tot == 0:
        return None
    # marginals and active set
    act = []; D1 = []; D0 = []
    for i in range(m):
        s1 = int(sum(Q[U] for U in range(N) if U >> i & 1))
        if s1 == 0: D0.append(i)
        elif s1 == tot: D1.append(i)
        else: act.append(i)
    r = len(act)
    # restrict to the active cube: coefficients on the face U_{D0}=0, U_{D1}=1
    base = sum(1 << i for i in D1)
    face = []
    for J in range(1 << r):
        U = base
        for k, i in enumerate(act):
            if J >> k & 1:
                U |= 1 << i
        face.append(int(W[U]))
    # in units of 2^{-r-1}: g restricted to R-cube has phihat(J) = W(U)/(2N); unit 2^{-r-1} = 1/(2 * 2^r)
    # phihat * 2^{r+1} = W * 2^{r+1} / (2N) = W * 2^{r} / N = W / 2^{m-r}
    sc = 1 << (m - r)
    assert all(abs(c) % sc == 0 for c in face)
    co = [abs(c) // sc for c in face]          # integers: |phihat| * 2^{r+1}
    assert all(c > 0 for c in co)
    nu = min(co)
    pq = []
    for k in range(r):
        a0 = co[0]; a1 = co[1 << k]
        p, q = max(a0, a1), min(a0, a1)
        g = gcd(p, q); p //= g; q //= g
        pq.append((p, q))
    prodq = 1
    for p, q in pq:
        prodq *= q
    assert nu % prodq == 0, ("a fails", row)
    nup = nu // prodq
    w = Fraction(int((V * V).sum()), 4 * N)
    rhs = Fraction(nup * nup, 4 ** (r + 1))
    for p, q in pq:
        rhs *= p * p + q * q
    assert w == rhs, ("b fails", row, w, rhs)
    # (c)
    qlaw = Q / tot
    Hq = -sum(x * math.log2(x) for x in qlaw if x > 0)
    lhs = -math.log2(float(w)) + Hq
    rhs_c = 2 - 2 * math.log2(nup) + sum(Ft(p, q) for p, q in pq)
    assert abs(lhs - rhs_c) < 1e-9, ("c fails", row, lhs, rhs_c)
    # (d),(e)
    odd_class = (co[0] % 2 == 1)
    assert all((c % 2 == 1) == odd_class for c in co)
    if odd_class:
        assert nup % 2 == 1 and all(p % 2 == 1 and q % 2 == 1 for p, q in pq), ("d odd fails", row)
    else:
        assert nup % 2 == 0, ("d even fails", row)
    # count half points in the R-cube (|g|=1/2 <=> |V| = 1); g depends on x_R only up to sign
    halfcount = sum(1 for x in range(N) if abs(row[x]) == 1)
    halfR = halfcount // (1 << (m - r))
    assert halfcount % (1 << (m - r)) == 0
    assert (halfR % 2 == 1) == odd_class, ("e fails", row)
    return r, tuple(sorted(pq)), nup, odd_class

def main():
    m = int(sys.argv[1])
    pkl = sys.argv[2] if m == 4 else None
    rows = RV.product_rows(m, pkl)
    pairs = Counter(); nus = Counter(); n = 0
    for row in rows:
        res = analyse(row, m)
        if res is None:
            continue
        n += 1
        r, pq, nup, odd = res
        for p, q in pq:
            pairs[(p, q)] += 1
        nus[(nup, odd)] += 1
    print("m", m, "nonzero product rows checked:", n, "all identities (a)-(e) hold")
    print("(p,q) pairs occurring:", sorted(pairs.items()))
    print("(nu', odd class) occurring:", sorted(nus.items()))

if __name__ == "__main__":
    main()
