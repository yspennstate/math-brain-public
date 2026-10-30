#!/usr/bin/env python3
import itertools
import sympy as sp

p = sp.symbols("p")
PTS = list(itertools.product([0, 1], repeat=3))
SETS = [frozenset(s) for r in range(4) for s in itertools.combinations(range(3), r)]
NONEMPTY = [S for S in SETS if S]

def value(mask, idx):
    return 1 if ((mask >> idx) & 1) else -1

def essential(mask, i):
    for idx, y in enumerate(PTS):
        y2 = list(y)
        y2[i] = 1-y2[i]
        j = PTS.index(tuple(y2))
        if value(mask, idx) != value(mask, j):
            return True
    return False

def coeff_sq(mask, S):
    # Exact square of the normalized common-p biased Fourier coefficient.
    num = 0
    for idx, y in enumerate(PTS):
        prob = sp.prod(p if bit else 1-p for bit in y)
        centered = sp.prod(y[i]-p for i in S)
        num += value(mask, idx)*prob*centered
    return sp.factor(sp.cancel(num**2/(p*(1-p))**len(S)))

def toric_numerators(mask):
    w = {S: coeff_sq(mask, S) for S in NONEMPTY}
    S = lambda *xs: frozenset(xs)
    equations = [
        w[S(0,1)]*w[S(2)] - w[S(0,2)]*w[S(1)],
        w[S(0,1)]*w[S(2)] - w[S(1,2)]*w[S(0)],
        w[S(0,1,2)]*w[S(0)] - w[S(0,1)]*w[S(0,2)],
    ]
    nums = [sp.factor(sp.fraction(sp.cancel(e))[0]) for e in equations]
    return w, nums

def common_gcd(nums):
    nz = [sp.Poly(e, p, domain=sp.QQ) for e in nums if sp.expand(e) != 0]
    if not nz:
        return sp.Integer(0)
    g = nz[0]
    for h in nz[1:]:
        g = sp.gcd(g, h)
    return sp.factor(g.as_expr())

ESSENTIAL = [m for m in range(256) if all(essential(m, i) for i in range(3))]
IDENTICAL = []
FACTOR_SET = set()
for mask in ESSENTIAL:
    _, nums = toric_numerators(mask)
    if all(sp.expand(e) == 0 for e in nums):
        IDENTICAL.append(mask)
    else:
        g = common_gcd(nums)
        _, factors = sp.factor_list(g, p)
        for f, _ in factors:
            f = sp.factor(f)
            if sp.degree(f, p) > 0 and f not in (p, p-1):
                FACTOR_SET.add(f)

EXPECTED_IDENTICAL = {
    *(1 << k for k in range(8)),
    *(255 ^ (1 << k) for k in range(8)),
    105, 150,
}
assert set(IDENTICAL) == EXPECTED_IDENTICAL
assert len(ESSENTIAL) == 218

EXPECTED_FACTORS = {
    8*p**2-8*p+1,
    2*p**2-1,
    8*p**2-8*p+3,
    2*p**2-2*p+1,
    2*p**2-4*p+1,
    18*p**2-24*p+7,
    2*p-3,
    2*p-1,
    2*p**2-6*p+3,
    18*p**2-12*p+1,
    2*p+1,
    2*p**2+2*p-1,
}
assert {sp.factor(x) for x in FACTOR_SET} == {sp.factor(x) for x in EXPECTED_FACTORS}

INTERIOR_FACTORS = []
for f in sorted(FACTOR_SET, key=str):
    roots = sp.solve(sp.Eq(f, 0), p)
    if any(r.is_real is True and bool(r > 0) and bool(r < 1) for r in roots):
        INTERIOR_FACTORS.append(f)

EXPECTED_INTERIOR = {
    2*p-1,
    8*p**2-8*p+1,
    2*p**2-1,
    2*p**2-4*p+1,
    18*p**2-24*p+7,
    2*p**2-6*p+3,
    18*p**2-12*p+1,
    2*p**2+2*p-1,
}
assert {sp.factor(x) for x in INTERIOR_FACTORS} == {sp.factor(x) for x in EXPECTED_INTERIOR}

# Exact exceptional witness: mask 7 at p=1/sqrt(2).
w7, e7 = toric_numerators(7)
assert sp.expand(e7[0]) == 0
assert sp.factor(e7[1] / (-16*p**3*(p-1)**5)) == 2*p**2-1
assert sp.factor(e7[2] / (-16*p**4*(p-1)**4)) == 2*p**2-1
r = sp.sqrt(2)/2
for coeff2 in w7.values():
    assert sp.simplify(coeff2.subs(p, r)) > 0
assert all(sp.simplify(e.subs(p, r)) == 0 for e in e7)

print("PASS")
print("essential_truth_tables =", len(ESSENTIAL))
print("identically_zero_toric_essential_masks =", IDENTICAL)
print("nonfamily_essential_count =", len(ESSENTIAL)-len(IDENTICAL))
print("all_common_gcd_nonboundary_factors =", sorted(map(str, FACTOR_SET)))
print("interior_exception_factors =", sorted(map(str, INTERIOR_FACTORS)))
print("mask7_toric_numerators =", list(map(str, e7)))
print("mask7_exception =", "p=sqrt(2)/2")
