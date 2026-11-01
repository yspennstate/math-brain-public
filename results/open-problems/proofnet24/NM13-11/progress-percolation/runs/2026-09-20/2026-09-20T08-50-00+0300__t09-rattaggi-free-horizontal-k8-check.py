from fractions import Fraction
from math import isqrt


def ceil_sqrt_frac(n: int, den: int = 1_000_000) -> Fraction:
    q = isqrt(n * den * den)
    if q * q <= n * den * den:
        q += 1
    return Fraction(q, den)


# p_c certificate on T_12 x T_8 using a depth-3 T_8-fibre exploration.
p = Fraction(7, 125)
s = 1 - p
h = s
for _ in range(1, 3):
    h = s * (s + p * h) ** 7
C3 = s * (s + p * h) ** 8
m3 = 11 * (1 - C3)
assert m3 > 1 + Fraction(1, 5000)

# Exact rational upper bounds for square roots entering the adjacency estimate.
r11 = ceil_sqrt_frac(11)
r7 = ceil_sqrt_frac(7)
assert r11 * r11 > 11
assert r7 * r7 > 7

# Certified p_u floors for k freely generating added inverse pairs.
floors = {
    4: Fraction(323, 5000),
    5: Fraction(31, 500),
    6: Fraction(299, 5000),
    7: Fraction(29, 500),
    8: Fraction(113, 2000),
}

print(f"pc_test={p}={float(p):.12f}")
print(f"depth3_mean={float(m3):.15f}")
print(f"depth3_mean_minus_1={float(m3 - 1):.15f}")
print("CERT depth3_mean > 1 + 1/5000")

for k, r in floors.items():
    t = 2 * k - 1
    root = isqrt(t)
    radd = Fraction(root, 1) if root * root == t else ceil_sqrt_frac(t)
    D = 20 + 2 * k
    Q = D - 1
    a_up = 2 * r11 + 2 * r7 + 2 * radd
    z = 1 / r
    margin = z + Fraction(Q, 1) / z - a_up
    assert z * z > Q
    assert margin > 0
    assert r > p
    print(
        f"k={k} D={D} pu>{r}={float(r):.12f} "
        f"gap>{float(r-p):.12f} root_margin={float(margin):.12f}"
    )

print("ALL_EXACT_CHECKS_PASS")
