from fractions import Fraction
from itertools import combinations, permutations
from math import sqrt, e


def det_frac(A):
    n = len(A)
    if n == 0:
        return Fraction(1)
    out = Fraction(0)
    for p in permutations(range(n)):
        inv = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        term = Fraction(1)
        for i, j in enumerate(p):
            term *= A[i][j]
        out += (-1 if inv % 2 else 1) * term
    return out


def e_k_minors(M, k):
    m, n = len(M), len(M[0])
    out = Fraction(0)
    for R in combinations(range(m), k):
        for C in combinations(range(n), k):
            d = det_frac([[Fraction(M[i][j]) for j in C] for i in R])
            out += d * d
    return out


def row_k_mass(M, i, k=3):
    m, n = len(M), len(M[0])
    out = Fraction(0)
    for R in combinations(range(m), k):
        if i not in R:
            continue
        for C in combinations(range(n), k):
            d = det_frac([[Fraction(M[a][b]) for b in C] for a in R])
            out += d * d
    return out


def frob2(M):
    return sum(Fraction(x) * Fraction(x) for row in M for x in row)


mats = [
    [[1, 0, 1, 2], [0, 1, 1, -1], [1, 1, 0, 1], [2, -1, 1, 0]],
    [[1, 2, 0, 1], [0, 1, 3, -1], [2, 0, 1, 1], [1, -1, 2, 2], [0, 2, -1, 1]],
    [[2, 0, 1, 0, 1], [1, 1, 0, 2, 0], [0, 1, 2, 0, 1], [1, 0, 1, 1, 2], [2, 1, 0, -1, 1]],
]

for q, M in enumerate(mats):
    Z = e_k_minors(M, 3)
    E2 = e_k_minors(M, 2)
    F2 = frob2(M)
    assert E2 <= F2 * F2 / 2
    for i in range(len(M)):
        rm = row_k_mass(M, i, 3)
        rn2 = sum(Fraction(x) * Fraction(x) for x in M[i])
        assert rm <= rn2 * F2 * F2 / 2
    print(f"matrix={q} E3={Z} E2={E2} F2={F2} row_norm_inequality=PASS")

# exact three-sample stability constants
eta = Fraction(1, 256)
tau = Fraction(128, 3969)
rho = eta + 5 * tau
assert rho == Fraction(167809, 1016064)
assert 2 * rho < Fraction(1, 2)

# improved Schur-mixture arithmetic
# (16/5)/3072^2 divided by (1/(16 sqrt(5)))^2 = 1/2304.
# Square away sqrt(5): rho_s^2/theta^4=1/1280.
ratio = Fraction(16, 5) * 1280 / (3072 ** 2)
assert ratio == Fraction(1, 2304)
# delta=1/(8 sqrt(6)) has delta^2/6 = 1/2304.
assert Fraction(1, 64 * 6) / 6 == Fraction(1, 2304)

print("rho0=", rho, float(rho))
print("three_sample_constant=", (9 * sqrt(3) * e / 2) * (1024 ** (1/6)))
print("four_core_partner_constant=", 3 * sqrt(e) * (4 / (1 - float(rho))) ** (1/6))
print("rank2_relative_distance=", sqrt(1 / (8 * sqrt(6))))
print("STATUS=QFORM_TRIPLE_VOLUME_PHYSICAL_BIANCHOR_CHECK_PASS")
