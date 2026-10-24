import math
from math import comb


def suspension(m):
    p = 2.0 ** (1 - m)
    ln2 = math.log(2.0)
    K_nat = 0.0
    L_nat = 0.0
    for j in range(m + 1):
        multiplicity = comb(m, j)
        P = (1 - p) ** 2 if j == 0 else p * p
        Q = (p ** j) * ((1 - p) ** (m - j))
        r = P / Q
        d = P * math.log(r) - P + Q
        h = (math.sqrt(P) - math.sqrt(Q)) ** 2
        weight = max(1.0, math.log(r) - 1.0)
        if weight * h > d + 2e-14:
            raise AssertionError((m, j, weight * h, d))
        K_nat += multiplicity * d
        L_nat += multiplicity * weight * h

    influence_excess = m * p
    A = math.sqrt(1 - p)
    B = math.sqrt(p)

    # Walsh eigenvalues of convolution by c=a+b.  At the exceptional
    # physical atom g_m=-1; all other atoms have g_m=+1.  The smallest
    # nonexceptional eigenvalue occurs with exactly one negative factor.
    zero_eigenvalue = -1.0 + 2.0 * (A ** m) - (A + B) ** m
    min_nonzero_eigenvalue = (
        1.0 + 2.0 * (A ** m) - (A + B) ** (m - 1) * (A - B)
    )
    return (
        K_nat / ln2,
        L_nat / ln2,
        influence_excess,
        zero_eigenvalue,
        min_nonzero_eigenvalue,
    )


print("m  K/I  L/I  (K-L)/I  zero_eig  min_nonzero_eig")
for m in (7, 8, 10, 12, 16, 20, 24, 28):
    K, L, I, z0, z1 = suspension(m)
    assert z0 < 0.0
    assert z1 > 0.0
    print(
        "%2d %.12f %.12f %.12f %.12f %.12f"
        % (m, K / I, L / I, (K - L) / I, z0, z1)
    )
print("PASS")
