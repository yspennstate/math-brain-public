from fractions import Fraction as F
from itertools import permutations


def add(z, w):
    return (z[0] + w[0], z[1] + w[1])


def mul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def scale(q, z):
    return (q * z[0], q * z[1])


def prod(xs):
    z = (F(1), F(0))
    for x in xs:
        z = mul(z, x)
    return z


def L(z):
    return -3 * z[0] - z[1]


def p(s):
    return tuple(int(c) - 1 for c in s)


def fmt(q):
    return f"{q.numerator}/{q.denominator}" if q.denominator != 1 else str(q.numerator)


a = [
    (F(-1, 100), F(76, 100)),
    (F(91, 100), F(-158, 100)),
    (F(1, 100), F(50, 100)),
    (F(161, 100), F(192, 100)),
]
b = [
    (F(-24, 100), F(48, 100)),
    (F(-69, 100), F(-103, 100)),
    (F(174, 100), F(159, 100)),
    (F(197, 100), F(-193, 100)),
]


def v(sig):
    return prod([add(a[i], b[sig[i]]) for i in range(4)])


vals = {sig: v(sig) for sig in permutations(range(4))}
scores = {sig: L(z) for sig, z in vals.items()}
M = max(scores.values())
maximizers = [sig for sig, s in scores.items() if s == M]
assert maximizers == [p("2341")]

u_num = (F(0), F(0))
for sig in map(p, ["3214", "4132", "3421", "2341"]):
    u_num = add(u_num, vals[sig])
u_num = add(u_num, scale(F(-1), vals[p("3241")]))
u = scale(F(1, 3), u_num)
gap = L(u) - M
assert gap == F(205137, 1250000)
assert gap > 0

print("UF_EXACT_COUNTEREXAMPLE PASS")
print("support_functional L(z)=-3 Re(z)-Im(z)")
print("unique_maximizer=2341")
print("M=" + fmt(M))
print("u_score=" + fmt(L(u)))
print("gap=" + fmt(gap))
print("u_complex_real=" + fmt(u[0]))
print("u_complex_imag=" + fmt(u[1]))

# Verify the one-parameter Birkhoff decomposition formula for S_3 on an exact
# rational test matrix.  The mathematical derivation in REPORT.md is general.
orders = [p("123"), p("231"), p("312"), p("132"), p("213"), p("321")]
lam = [F(1, 10), F(1, 5), F(3, 20), F(1, 20), F(1, 4), F(1, 4)]
assert sum(lam, F(0)) == 1
R = [[F(0) for _ in range(3)] for __ in range(3)]
for w, sig in zip(lam, orders):
    for i, j in enumerate(sig):
        R[i][j] += w

Lbd = max(F(0), R[2][2] - R[0][1], R[1][1] - R[0][2])
Ubd = min(R[0][0], R[1][1], R[2][2])
assert Lbd <= Ubd


def decomp(x):
    return [
        x,
        R[0][1] - R[2][2] + x,
        R[0][2] - R[1][1] + x,
        R[0][0] - x,
        R[2][2] - x,
        R[1][1] - x,
    ]


for x in (Lbd, Ubd):
    ls = decomp(x)
    assert min(ls) >= 0 and sum(ls, F(0)) == 1
    RR = [[F(0) for _ in range(3)] for __ in range(3)]
    for w, sig in zip(ls, orders):
        for i, j in enumerate(sig):
            RR[i][j] += w
    assert RR == R

print("S3_BIRKHOFF_INTERVAL PASS")
print("interval=[" + fmt(Lbd) + "," + fmt(Ubd) + "]")
