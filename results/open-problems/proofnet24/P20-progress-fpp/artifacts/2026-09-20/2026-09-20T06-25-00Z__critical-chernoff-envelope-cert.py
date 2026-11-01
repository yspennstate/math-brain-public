#!/usr/bin/env python3
from fractions import Fraction

# P04 strip-6 axis constant and local-SAW counting constants.
A = Fraction(1903, 1000)
B = Fraction(2837, 1000)
r = Fraction(4999, 1000)
a6 = Fraction(
    57444100690415803497507130042889304438078500562657949173917,
    94434081367035184054991164646261870153788595690449920000000,
)
C_old = Fraction(
    35548730504621175912805033436058585575537199210,
    530548441769990085527241493316853229845841,
)

# Near-critical Chernoff choice for the new cone slope rho=314/183.
rho = Fraction(314, 183)
s = Fraction(399901, 100000)  # 3.99901 > r-1 = 3.999
c = Fraction(608307, 1000000)
q = r / (1 + s)

# The old s=4 constant satisfies C_old = K/(1-4999/5000)=5000*K.
K = C_old / 5000
C_new = K / (1 - q)


def log_lower(z: Fraction, N: int = 20) -> Fraction:
    """Rigorous lower bound for log(z), z>1, via the positive atanh series."""
    assert z > 1
    t = (z - 1) / (z + 1)
    total = Fraction(0)
    p = t
    for k in range(N):
        total += p / (2 * k + 1)
        p *= t * t
    return 2 * total


LA = log_lower(A, 20)
LB = log_lower(B, 20)
LQ = log_lower(1 / q, 20)

# beta = exp(s*c) A^{-1} B^{-rho} q^{1+rho}.
# Multiplying by 183 and using log(q)=-log(1/q),
# 183 log beta <= U because LA,LB,LQ are lower log bounds.
U = 183 * s * c - 183 * LA - 314 * LB - 497 * LQ
d = Fraction(29, 5_000_000)

gap = c - a6
delta = 2 * gap

assert q == Fraction(499900, 499901)
assert rho < Fraction(429, 250)
assert s > r - 1
assert gap > 0
assert U < 0
assert U <= -183 * d  # hence log(beta) <= -29/5,000,000

# Finite residual positivity at m=an=5,000,000:
# beta^m <= exp(-29), so it suffices that exp(29) > c*C_new/gap.
ratio = c * C_new / gap


def exp_lower(x: Fraction, N: int) -> Fraction:
    term = Fraction(1)
    total = term
    for k in range(1, N + 1):
        term *= x / k
        total += term
    return total


E29 = exp_lower(Fraction(29), 80)
assert E29 > ratio
finite_margin = gap - c * C_new / E29
assert finite_margin > 0

# Same-slope improvement at P04's old rational boundary 429/250.
rho_old = Fraction(429, 250)
c_old_improved = Fraction(121669, 200000)  # 0.608345
U_old = (
    250 * s * c_old_improved
    - 250 * LA
    - 429 * LB
    - 679 * LQ
)
assert U_old <= -250 * Fraction(13, 1_000_000)
gap_old = c_old_improved - a6
delta_old = 2 * gap_old
C_ratio_old = c_old_improved * C_new / gap_old
E26 = exp_lower(Fraction(26), 80)
assert E26 > C_ratio_old
finite_margin_old = gap_old - c_old_improved * C_new / E26
assert finite_margin_old > 0

print("P20-T10-CRITICAL-CHERNOFF-CERT: ALL_EXACT_CHECKS_PASS")
print("rho_new =", rho, "=", float(rho))
print("rho_old =", rho_old, "=", float(rho_old))
print("s =", s, "=", float(s))
print("q =", q, "=", float(q))
print("c_new =", c, "=", float(c))
print("a6 =", a6, "=", float(a6))
print("new gap c-a6 =", gap, "=", float(gap))
print("new reflected defect coefficient 2(c-a6) =", delta, "=", float(delta))
print("C_new =", C_new, "=", float(C_new))
print("183*log(beta_new) upper U =", U, "=", float(U))
print("certified log(beta_new) <= -29/5000000 =", float(-d))
print("m=5,000,000 exp(29) Taylor lower / required ratio =", float(E29), "/", float(ratio))
print("finite normalized residual margin at m=5,000,000 =", float(finite_margin))
print("old-boundary improved c =", c_old_improved, "=", float(c_old_improved))
print("old-boundary improved defect coefficient =", delta_old, "=", float(delta_old))
print("certified log(beta_oldboundary) <= -13/1000000")
print("m=2,000,000 finite normalized residual margin at old boundary =", float(finite_margin_old))
