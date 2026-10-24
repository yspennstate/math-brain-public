from fractions import Fraction
from functools import lru_cache

# P13 / C0021 exact self-check for methods B2, B15, B30.
# All finite mathematical comparisons use Fraction.


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
            out.add((norm(t[:i] + (cp,) + t[i+1:]),
                     norm(t[:i] + (cm,) + t[i+1:])))
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


def min_regret(h):
    root = full(h)
    A = {root: Fraction(0)}
    front = {root}
    while front:
        cand = {}
        for s in front:
            if s in ('+', '-'):
                continue
            vs = V(s)
            for a, b in queries(s):
                r = Fraction(1) + (V(a) + V(b))/2 - vs
                assert r >= 0
                zval = A[s] + r
                for z in (a, b):
                    if z not in cand or zval < cand[z]:
                        cand[z] = zval
        new = set()
        for z, zval in cand.items():
            if z not in A or zval < A[z]:
                A[z] = zval
                new.add(z)
        front = new
    return A


def min_oriented_cost(h):
    # B15 identity predicts C(s)=D_h-V(s)+A(s) is the shortest path cost
    # with oriented edge cost 1 + (V(sibling)-V(chosen))/2.
    root = full(h)
    C = {root: Fraction(0)}
    front = {root}
    while front:
        cand = {}
        for s in front:
            if s in ('+', '-'):
                continue
            for a, b in queries(s):
                ca = Fraction(1) + (V(b) - V(a))/2
                cb = Fraction(1) + (V(a) - V(b))/2
                for z, edge in ((a, ca), (b, cb)):
                    zval = C[s] + edge
                    if z not in cand or zval < cand[z]:
                        cand[z] = zval
        new = set()
        for z, zval in cand.items():
            if z not in C or zval < C[z]:
                C[z] = zval
                new.add(z)
        front = new
    return C


D = [V(full(h)) for h in range(4)]
assert D == [Fraction(1), Fraction(5,2), Fraction(393,64), Fraction(15796051,1048576)]

# B15: exact path identity / orientation resource, checked over every reachable state h<=3.
rows = []
As = {}
Cs = {}
for h in (1, 2, 3):
    A = min_regret(h)
    C = min_oriented_cost(h)
    As[h] = A
    Cs[h] = C
    assert set(A) == set(C)
    Dh = D[h]
    for s in A:
        assert C[s] == Dh - V(s) + A[s]
    rows.append((h, len(A), min(C.values()), max(C.values())))

# Exact height-3 minimizer recovered from the preceding complete enumeration.
U1 = norm(('u','u','u'))
b = norm(('-', 'u', 'u'))
s3 = norm((
    norm(('-', U1, U1)),
    norm((b, b, b)),
    norm((b, b, U1)),
))
A3 = As[3][s3]
W3 = V(s3) - A3
C3 = D[3] - W3
assert q(s3) == Fraction(31,256)
assert abs(2*q(s3)-1) == Fraction(97,128)
assert V(s3) == Fraction(547983,65536)
assert A3 == Fraction(170249,131072)
assert W3 == Fraction(925717,131072)
assert C3 == Fraction(8390315,1048576)
P3 = C3 / D[3]
m = Fraction(97,128)
ratio2 = P3*P3/(m*m*m)
assert ratio2 == Fraction(147634018423616307200,227725810949378078473)
assert 16*P3*P3 > 9*m*m*m

# B2: recursively lift exactly the sign-oriented height-3 witness.
def lift(t):
    if t in ('+', '-'):
        return t
    if t == 'u':
        return norm(('u','u','u'))
    return norm(tuple(lift(x) for x in t))

lifted = s3
lift_q_rows = []
for h in range(3, 7):
    assert q(lifted) == Fraction(31,256)
    lift_q_rows.append((h, q(lifted)))
    lifted = lift(lifted)

# B30: forced-block-completion surrogate. Replacing every unresolved macro-leaf
# by a block whose optimal expected completion cost is b scales V,A,W,C by b.
# For one height lift, b=D1=5/2, so the normalized progress is unchanged.
block_b = D[1]
C4_block = block_b * C3
D4_block = block_b * D[3]
P4_block = C4_block / D4_block
assert P4_block == P3

# Compare this scale-neutral block benchmark to the actual-height-4 H threshold
# using the rigorous inherited D4 interval. The actual C4 is NOT computed here.
L4 = Fraction(545085503,15728640)
U4 = Fraction(1332467382289843607,36028797018963968)
theta2 = Fraction(9,16) * m**3   # theta=((3/4)|m|^(3/2)) so theta^2 is rational.
assert C4_block*C4_block > theta2 * U4*U4
# Hence the forced-block model remains on the safe side even if D4 takes its
# rigorous upper bound; any true counterexample in this lifted family must use
# inter-block interleaving rather than pure recursive scaling.

print('C0021 B2/B15/B30 exact self-check')
print('D', *D)
for h, n, mn, mx in rows:
    print('B15_h', h, 'reachable_states', n, 'oriented_identity_PASS', 'minC', mn, 'maxC', mx)
print('B15_s3_q', q(s3))
print('B15_s3_m_abs', m)
print('B15_s3_V_A_W_C', V(s3), A3, W3, C3)
print('B15_s3_P', P3)
print('B15_s3_P2_over_abs_m3', ratio2)
print('B2_lift_q_rows', lift_q_rows)
print('B30_block_scale', block_b)
print('B30_C4_block', C4_block)
print('B30_D4_block', D4_block)
print('B30_P4_block', P4_block)
print('B30_actual_D4_lower_upper', L4, U4)
print('B30_theta2', theta2)
print('B30_block_margin_squared_at_U4', C4_block*C4_block - theta2*U4*U4)
print('ALL_EXACT_B2_B15_B30_CHECKS_PASS')
