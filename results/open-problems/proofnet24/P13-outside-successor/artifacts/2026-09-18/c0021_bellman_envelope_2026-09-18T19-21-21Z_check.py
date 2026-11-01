from fractions import Fraction
from functools import lru_cache
from itertools import combinations_with_replacement

# Exact self-check for P13 / C0021, 2026-09-18.
# It verifies the Bellman-regret concave-envelope theorem's finite inputs
# through child height h=3 using only Fraction arithmetic.

def norm(ch):
    p = sum(c == '+' for c in ch)
    m = sum(c == '-' for c in ch)
    if p >= 2:
        return '+'
    if m >= 2:
        return '-'
    return tuple(sorted(ch, key=repr))

@lru_cache(None)
def queries(t):
    if t == 'u':
        return (('+', '-'),)
    if t in ('+', '-'):
        return ()
    out = set()
    for i, c in enumerate(t):
        if i and t[i] == t[i-1]:
            continue
        for cp, cm in queries(c):
            out.add((
                norm(t[:i] + (cp,) + t[i+1:]),
                norm(t[:i] + (cm,) + t[i+1:])
            ))
    return tuple(sorted(out, key=repr))

@lru_cache(None)
def V(t):
    if t in ('+', '-'):
        return Fraction(0)
    return min(Fraction(1) + (V(a) + V(b))/2 for a, b in queries(t))

@lru_cache(None)
def q(t):
    if t == '+':
        return Fraction(1)
    if t == '-':
        return Fraction(0)
    if t == 'u':
        return Fraction(1, 2)
    a, b, c = (q(x) for x in t)
    return a*b + a*c + b*c - 2*a*b*c

def full(h):
    return 'u' if h == 0 else norm((full(h-1),)*3)

def canonical_levels(max_h):
    levels = [{'+', '-', 'u'}]
    for _ in range(max_h):
        prev = sorted(levels[-1], key=repr)
        out = {'+', '-'}
        for a, b, c in combinations_with_replacement(prev, 3):
            out.add(norm((a, b, c)))
        levels.append(out)
    return levels

def min_regret(h):
    """A_h(s): minimum accumulated local Bellman regret from full(h) to s."""
    root = full(h)
    A = {root: Fraction(0)}
    front = {root}
    while front:
        candidates = {}
        for s in front:
            if s in ('+', '-'):
                continue
            vs = V(s)
            for a, b in queries(s):
                r = Fraction(1) + (V(a)+V(b))/2 - vs
                assert r >= 0
                cand = A[s] + r
                for z in (a, b):
                    if z not in candidates or cand < candidates[z]:
                        candidates[z] = cand
        new_front = set()
        for z, cand in candidates.items():
            if z not in A or cand < A[z]:
                A[z] = cand
                new_front.add(z)
        front = new_front
    return A

def least_concave_majorant(points):
    """Upper concave hull for finite points sorted by x."""
    hull = []
    for p in sorted(points):
        hull.append(p)
        while len(hull) >= 3:
            x1, y1 = hull[-3]
            x2, y2 = hull[-2]
            x3, y3 = hull[-1]
            s12 = (y2-y1)/(x2-x1)
            s23 = (y3-y2)/(x3-x2)
            if s12 < s23:  # violates decreasing slopes
                hull.pop(-2)
            else:
                break
    return hull

def interp(hull, x):
    for (x1,y1),(x2,y2) in zip(hull, hull[1:]):
        if x1 <= x <= x2:
            return y1 + (y2-y1)*(x-x1)/(x2-x1)
    if x == hull[-1][0]:
        return hull[-1][1]
    raise AssertionError("x outside hull")

levels = canonical_levels(3)
assert [len(levels[h]) for h in range(4)] == [3, 6, 46, 17206]

D = [V(full(h)) for h in range(4)]
assert D == [
    Fraction(1),
    Fraction(5,2),
    Fraction(393,64),
    Fraction(15796051,1048576),
]

expected_rho = [
    Fraction(1,2),
    Fraction(3,5),
    Fraction(585,917),
    Fraction(165736792,236940765),
]
expected_failures = [0,0,2,146]
expected_lower_next = [
    Fraction(5,2),
    Fraction(6),
    Fraction(3249,224),
    Fraction(545085503,15728640),
]

rows = []
As = []
hulls = []
raw_hulls = []
for h in range(4):
    A = min_regret(h)
    As.append(A)
    assert set(A) == levels[h]
    by_m = {}
    raw_by_m = {}
    failures = []
    for s, a in A.items():
        m = 2*q(s)-1
        g = (V(s)-a)/D[h]
        raw = V(s)/D[h]
        by_m[m] = max(by_m.get(m, Fraction(-10)), g)
        raw_by_m[m] = max(raw_by_m.get(m, Fraction(-10)), raw)
        if s not in ('+', '-'):
            lhs = V(s)-a
            rhs = D[h]*(1-m*m)
            if lhs > rhs:
                failures.append((lhs-rhs, s, lhs, rhs, m, a, V(s)))
    hull = least_concave_majorant(by_m.items())
    raw_hull = least_concave_majorant(raw_by_m.items())
    hulls.append(hull)
    raw_hulls.append(raw_hull)
    rho = interp(hull, Fraction(-1,2))
    raw_rho = interp(raw_hull, Fraction(-1,2))
    lower_next = (3-rho)*D[h]
    assert rho == expected_rho[h]
    assert len(failures) == expected_failures[h]
    assert lower_next == expected_lower_next[h]
    rows.append((h, len(levels[h]), D[h], rho, raw_rho, lower_next, len(hull), len(failures)))

# Exact h=2 counterexample to the tempting pointwise uncertainty bound.
s2 = norm(('+', norm(('+','u','u')), norm(('+','u','u'))))
A2 = As[2][s2]
m2 = 2*q(s2)-1
lhs2 = V(s2)-A2
rhs2 = D[2]*(1-m2*m2)
assert m2 == Fraction(7,8)
assert V(s2) == Fraction(15,8)
assert A2 == Fraction(3,8)
assert lhs2 == Fraction(3,2)
assert rhs2 == Fraction(5895,4096)
assert lhs2-rhs2 == Fraction(249,4096)

# The two exact h=3 hull vertices bracketing -1/2 certify rho_3 by interpolation.
H3 = hulls[3]
left = (Fraction(-293,512), Fraction(10088708,15796051))
right = (Fraction(-31,64), Fraction(11256776,15796051))
assert left in H3 and right in H3
assert left[0] < Fraction(-1,2) < right[0]
assert interp(H3, Fraction(-1,2)) == Fraction(165736792,236940765)

print("C0021 Bellman-regret concave-envelope exact self-check")
for h,n,Dh,rho,rawrho,L,hv,fc in rows:
    print("h",h,
          "states",n,
          "D_h",Dh,
          "rho_regret",rho,
          "rho_raw",rawrho,
          "lower_D_(h+1)",L,
          "hull_vertices",hv,
          "pointwise_uncertainty_failures",fc)
print("h2_pointwise_counterexample_state", repr(s2))
print("h2_m",m2)
print("h2_V",V(s2))
print("h2_A",A2)
print("h2_V_minus_A",lhs2)
print("h2_D_times_1_minus_m2",rhs2)
print("h2_excess",lhs2-rhs2)
print("h3_bracketing_left",left)
print("h3_bracketing_right",right)
print("h3_rho_exact",expected_rho[3])
print("h3_D4_lower_exact",expected_lower_next[3])
print("ALL_EXACT_BELLMAN_ENVELOPE_CHECKS_PASS")
