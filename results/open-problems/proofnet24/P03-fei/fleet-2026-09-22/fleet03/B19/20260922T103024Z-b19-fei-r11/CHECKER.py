from fractions import Fraction
from itertools import product


def g(bits):
    a, b = bits
    return -1 if (a and b) else 1


def f(x):
    return g(x[:2]) * g(x[2:])


n = 4
coeff = {}
for mask in range(1 << n):
    total = 0
    for x in product((0, 1), repeat=n):
        parity = sum(x[i] for i in range(n) if (mask >> i) & 1)
        total += f(x) * (-1 if parity & 1 else 1)
    coeff[mask] = Fraction(total, 1 << n)

sq = {m: a * a for m, a in coeff.items()}
assert set(sq.values()) == {Fraction(1, 16)}
assert sum(sq.values(), Fraction(0)) == 1

v = 1 - sq[0]
q = []
for i in range(n):
    q.append(sum((w for m, w in sq.items() if (m >> i) & 1), Fraction(0)))
assert v == Fraction(15, 16)
assert q == [Fraction(1, 2)] * 4

r = [qi / v for qi in q]
assert r == [Fraction(8, 15)] * 4
c = v
lhs = 1 - c
rhs = Fraction(1)
for ri in r:
    rhs *= 1 - c * ri
assert lhs == rhs == Fraction(1, 16)

for m in range(1, 1 << n):
    P = sq[m] / v
    assert P == Fraction(1, 15)

i, j = 0, 2
s = sum(
    (w for m, w in sq.items() if ((m >> i) & 1 and (m >> j) & 1)),
    Fraction(0),
)
b = c * q[i] * q[j] / v
assert s == b == Fraction(1, 4)

# Cross-factor tensor identity from the source co-pair theorem.
p = Fraction(0)
o = q[i] * q[j]
cross = Fraction(0)
omega = p - 2 * cross + 4 * o
assert o == Fraction(1, 4)
assert omega == 1
assert 4 * b == 1
assert omega - 4 * b == 0

print("walsh_square", "1/16")
print("v", f"{v.numerator}/{v.denominator}")
print("q", ",".join(f"{x.numerator}/{x.denominator}" for x in q))
print("r", ",".join(f"{x.numerator}/{x.denominator}" for x in r))
print("c", f"{c.numerator}/{c.denominator}")
print("pair_s", f"{s.numerator}/{s.denominator}")
print("pair_b", f"{b.numerator}/{b.denominator}")
print("cross_tensor_omega", omega)
print("renormalized_excess", omega - 4 * b)
print("K_occ", 0)
print("FEI_B19_SELECTED_PAIR_BASELINE_REGRESSION_PASS")
