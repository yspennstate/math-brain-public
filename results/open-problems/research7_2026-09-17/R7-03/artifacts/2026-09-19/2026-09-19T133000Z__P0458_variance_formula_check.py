from fractions import Fraction
from itertools import permutations
from math import comb

# Exact Fraction-arithmetic self-check for
# 2026-09-19T133000Z__P0458_exact_finite_variance_projection.md.
# This is owner-track validation, not an independent audit.

def padd(a, b):
    n = max(len(a), len(b))
    c = [Fraction(0) for _ in range(n)]
    for i, x in enumerate(a): c[i] += x
    for i, x in enumerate(b): c[i] += x
    while len(c) > 1 and c[-1] == 0: c.pop()
    return c

def pscale(a, s):
    return [x*s for x in a]

def pmul(a, b):
    c = [Fraction(0) for _ in range(len(a)+len(b)-1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    while len(c) > 1 and c[-1] == 0: c.pop()
    return c

def pint(a):
    return [Fraction(0)] + [a[i]/Fraction(i+1) for i in range(len(a))]

def pdivx(a):
    assert a[0] == 0
    return a[1:]

def one_minus_pow(m):
    return [Fraction(((-1)**j)*comb(m, j)) for j in range(m+1)]

def beta_cdf_poly(k, r):
    # I_x(k,r)=sum_{j=k}^{k+r-1} C(k+r-1,j)x^j(1-x)^(k+r-1-j)
    N = k+r
    out = [Fraction(0)]
    for j in range(k, N):
        term = [Fraction(0)]*j + [Fraction(comb(N-1, j))]
        term = pmul(term, one_minus_pow(N-1-j))
        out = padd(out, term)
    return out

def beta_monomial_expectation(j, a, b):
    # B(a+j,b)/B(a,b)
    z = Fraction(1)
    for t in range(j):
        z *= Fraction(a+t, a+b+t)
    return z

def ebeta(poly, a, b):
    return sum(c*beta_monomial_expectation(j, a, b)
               for j, c in enumerate(poly))

def exact_formula(n, k):
    r = n-1-k
    assert n >= 4 and 2 <= k <= n-2 and r >= 1
    F = beta_cdf_poly(k, r)
    intF = pint(F)
    Q = pdivx(intF)

    xF = [Fraction(0)] + F
    xQ = [Fraction(0)] + Q
    J1 = padd(xF, pscale(xQ, -1))

    F2 = pmul(F, F)
    J2 = padd(
        padd([Fraction(0)] + F2,
             pscale(pmul(F, intF), -2)),
        pint(F2),
    )
    numer_b = padd(J2, pscale(pmul(J1, J1), -1))
    assert numer_b[0] == 0 and numer_b[1] == 0
    bpoly = [c/Fraction((n-2)**2) for c in numer_b[2:]]

    EQ = ebeta(Q, k+1, r)
    EQ2 = ebeta(pmul(Q, Q), k+1, r)
    Eb = ebeta(bpoly, k+1, r)
    delta = Fraction(k)*EQ
    varD = delta - delta*delta + Fraction(k*(k-1))*(EQ2+Eb)
    return delta, varD

def degree_from_order(n, k, perm):
    edges = [(i,j) for i in range(n) for j in range(i+1,n)]
    rank = {edges[eidx]: pos for pos, eidx in enumerate(perm)}
    prefs = []
    for i in range(n):
        inc = []
        for j in range(n):
            if i == j: continue
            e = tuple(sorted((i,j)))
            inc.append((rank[e], j))
        inc.sort()
        prefs.append({j for _, j in inc[:k]})
    return sum(1 for j in range(1,n) if j in prefs[0] and 0 in prefs[j])

# Check the exact all-(n,k) formula against the independently derived r=1 identities.
count = 0
for n in range(4, 31):
    k = n-2
    delta, varD = exact_formula(n, k)
    delta_ref = Fraction(n-2, 2*n-3)
    var_ref = Fraction(7*n*n - 27*n + 24, 3*(2*n-3)**2)
    assert delta == delta_ref, (n, delta, delta_ref)
    assert varD == var_ref, (n, varD, var_ref)
    count += 1
print(f"R1_REFERENCE_CASES_PASS={count}")

# Exhaustive model-level check for K4,k=2 over every strict global edge order.
n, k = 4, 2
m = comb(n, 2)
vals = [degree_from_order(n, k, p) for p in permutations(range(m))]
mean_enum = Fraction(sum(vals), len(vals))
var_enum = sum((Fraction(v)-mean_enum)**2 for v in vals) / len(vals)
delta, var_formula = exact_formula(n, k)
assert mean_enum == k-delta
assert var_enum == var_formula
print(f"K4_K2_EDGE_ORDERS_PASS={len(vals)}")
print(f"K4_K2_MEAN={mean_enum}")
print(f"K4_K2_VARIANCE={var_enum}")
print("ALL_EXACT_CHECKS_PASS")
