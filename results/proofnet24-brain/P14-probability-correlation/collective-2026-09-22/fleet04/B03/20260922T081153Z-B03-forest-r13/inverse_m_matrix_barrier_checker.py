from fractions import Fraction as F


def case(t, q=5):
    a = t * t
    U = V = W = F(q) * a
    Lam = F(q)
    sd = F(1) - U
    so = a - W
    eig_small = sd + so
    eig_large = sd - so
    det = sd * sd - so * so
    lhs = a * (2 * Lam - 1)
    return {
        "t": t,
        "a": a,
        "U": U,
        "V": V,
        "W": W,
        "Lambda": Lam,
        "schur_diag": sd,
        "schur_off": so,
        "eig_small": eig_small,
        "eig_large": eig_large,
        "det": det,
        "lhs": lhs,
    }


def fmt(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


cases = [case(F(1, 3)), case(F(1, 4))]
for c in cases:
    print(
        " ".join(
            f"{k}={fmt(v)}" for k, v in c.items()
        )
    )

c = cases[0]
assert c["a"] == F(1, 9)
assert c["U"] == c["V"] == c["W"] == F(5, 9)
assert c["Lambda"] == 5
assert c["schur_diag"] == F(4, 9)
assert c["schur_off"] == F(-4, 9)
assert c["eig_small"] == 0
assert c["eig_large"] == F(8, 9)
assert c["det"] == 0
assert c["lhs"] == 1

c = cases[1]
assert c["a"] == F(1, 16)
assert c["U"] == c["V"] == c["W"] == F(5, 16)
assert c["Lambda"] == 5
assert c["schur_diag"] == F(11, 16)
assert c["schur_off"] == F(-1, 4)
assert c["eig_small"] == F(7, 16)
assert c["eig_large"] == F(15, 16)
assert c["det"] == F(105, 256)
assert c["lhs"] == F(9, 16)

print("STATUS=PASS")
