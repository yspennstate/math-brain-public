from fractions import Fraction


def walsh(vals):
    N = len(vals)
    out = []
    for s in range(N):
        sm = 0
        for x, v in enumerate(vals):
            sm += v * (-1 if ((s & x).bit_count() & 1) else 1)
        out.append(Fraction(sm, N))
    return out


# Exact three-bit selector from REPORT.md, Section 5:
# f=1 if x3=-1; f=x1*x2 if x3=+1.
vals = []
for b in range(8):
    x1 = 1 if ((b >> 0) & 1) == 0 else -1
    x2 = 1 if ((b >> 1) & 1) == 0 else -1
    x3 = 1 if ((b >> 2) & 1) == 0 else -1
    vals.append(1 if x3 == -1 else x1 * x2)

a = walsh(vals)
assert a == [
    Fraction(1, 2), Fraction(0), Fraction(0), Fraction(1, 2),
    Fraction(-1, 2), Fraction(0), Fraction(0), Fraction(1, 2),
]
p = [z * z for z in a]
V = 1 - p[0]
q = [Fraction(0)] * 8
for s in range(1, 8):
    q[s] = p[s] / V
assert V == Fraction(3, 4)
assert q[3] == q[4] == q[7] == Fraction(1, 3)
assert sum(q) == 1
m1 = sum(q[s] for s in range(1, 8) if s & 1)
m2 = sum(q[s] for s in range(1, 8) if s & 2)
j12 = sum(q[s] for s in range(1, 8) if (s & 1) and (s & 2))
cov12 = j12 - m1 * m2
assert (m1, m2, j12, cov12) == (
    Fraction(2, 3), Fraction(2, 3), Fraction(2, 3), Fraction(2, 9)
)


# Exact one-point formulas from REPORT.md, Section 4.
def one_point(n):
    N = 1 << n
    V = Fraction(4 * (N - 1), N * N)
    I = Fraction(2 * n, N)
    EK2 = Fraction(n * (n + 1), N)
    var = EK2 - I * I
    efact2 = Fraction(n * (n - 1), N)
    return {
        "n": n,
        "N": N,
        "V": V,
        "I": I,
        "var": var,
        "var_over_I": var / I,
        "factorial2": efact2,
        "factorial2_over_I2": efact2 / (I * I),
    }


expected = {
    4: (Fraction(2), Fraction(3)),
    8: (Fraction(71, 16), Fraction(56)),
    16: (Fraction(17407, 2048), Fraction(15360)),
}
for n, pair in expected.items():
    row = one_point(n)
    assert (row["var_over_I"], row["factorial2_over_I2"]) == pair

print("selector_covariance", cov12)
for n in (4, 8, 16):
    row = one_point(n)
    print(
        "one_point",
        n,
        "var_over_I",
        row["var_over_I"],
        "factorial2_over_I2",
        row["factorial2_over_I2"],
    )
print("all_exact_checks_passed")
