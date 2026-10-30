from fractions import Fraction
from itertools import combinations
import math


def ek(vals, k):
    total = Fraction(0)
    for inds in combinations(range(len(vals)), k):
        p = Fraction(1)
        for i in inds:
            p *= vals[i]
        total += p
    return total


def sylvester(n):
    H = [[1]]
    while len(H) < n:
        top = [r + r for r in H]
        bot = [r + [-x for x in r] for r in H]
        H = top + bot
    return H


# Exact Hadamard check for the dense rotated example.
H = sylvester(8)
for i in range(8):
    for j in range(8):
        dot = sum(H[i][k] * H[j][k] for k in range(8))
        assert dot == (8 if i == j else 0)

# Squared singular values of M = diag(1,1,1,1,1/16,...,1/16) H_8/sqrt(8).
x = [Fraction(1)] * 4 + [Fraction(1, 256)] * 4
E3 = ek(x, 3)
E4 = ek(x, 4)
H12 = ek(x[2:], 2)
assert E3 == Fraction(17171969, 4194304)
assert E4 == Fraction(4565766145, 4294967296)
assert H12 == Fraction(33795, 32768)

# Constants in the row-marginal-free pair-promotion theorem.
C_pair_unit = 2 ** (17 / 8)
C_triple_after_half = 2 ** (15 / 8)
C_rank4_after_quarter = 2 ** (7 / 4)
assert C_triple_after_half < C_pair_unit
assert C_rank4_after_quarter < C_pair_unit

# Designated-partner pair mass eta > 2/75.
C_partner = C_pair_unit * (Fraction(75, 2) ** Fraction(1, 8))
C_partner_expected = 4 * (75 ** (1 / 8))
assert abs(float(C_partner) - C_partner_expected) < 1e-12

# Explicit dense indefinite example.
C_example = C_pair_unit * float(H12) ** (-1 / 8)
C_E3 = 8.453021225528176 * float(E3) ** (-1 / 6)
C_E4 = 7.659094523616393 * float(E4) ** (-1 / 8)
C_rank8 = (8 / 6) * (65536 ** (1 / 8))
assert C_example < C_rank8 < C_E3 < C_E4

print("QFORM_B04_R48_PAIR_ANCHORED_PROMOTION_CHECK_PASS")
print("E3=", E3, float(E3))
print("E4=", E4, float(E4))
print("H12=", H12, float(H12))
print("C_pair_unit=", C_pair_unit)
print("C_partner=", float(C_partner))
print("C_example=", C_example)
print("C_rank8=", C_rank8)
print("C_E3=", C_E3)
print("C_E4=", C_E4)
