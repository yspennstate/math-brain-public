"""Independent exact arithmetic checks for w364's four-edge example."""
from fractions import Fraction
from itertools import product

rows = []
for a1, a2, b1, b2 in product((1, 2), repeat=4):
    t = min(a1 + b1, a2 + b2)
    ell = min(a1, a2) + min(b1, b2)
    rows.append((t, ell, t - ell))

def mean(xs):
    return sum(map(Fraction, xs), Fraction(0)) / len(xs)

def var(xs):
    m = mean(xs)
    return mean([(Fraction(x) - m) ** 2 for x in xs])

t = [r[0] for r in rows]
ell = [r[1] for r in rows]
g = [r[2] for r in rows]
cov = mean([(Fraction(x) - mean(ell)) * (Fraction(y) - mean(g)) for x, y in zip(ell, g)])
assert len(rows) == 16
assert {v: t.count(v) for v in (2, 3, 4)} == {2: 7, 3: 8, 4: 1}
assert {v: ell.count(v) for v in (2, 3, 4)} == {2: 9, 3: 6, 4: 1}
assert g.count(1) == 2 and g.count(0) == 14
assert mean(t) == Fraction(21, 8) and var(t) == Fraction(23, 64)
assert mean(ell) == Fraction(5, 2) and var(ell) == Fraction(3, 8)
assert mean(g) == Fraction(1, 8) and var(g) == Fraction(7, 64)
assert cov == Fraction(-1, 16)
print("PASS 16 configurations; T counts 7/8/1; L counts 9/6/1; Var(T)=23/64; Var(L)=3/8; Cov(L,G)=-1/16")
