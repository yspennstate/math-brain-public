from fractions import Fraction as F

# Independent exact-arithmetic audit for C27-SUM-756.
# For K=2,...,63 we replace n^{-1/2} by a rational upper bound m/D,
# where m is the least integer satisfying n*m^2 >= D^2.  Therefore every
# computed Sbar_K is a rigorous rational upper bound for C27's S_K.

D = 10**12
TARGET = F(26, 25)


def up_inv_sqrt(n: int) -> F:
    lo, hi = 0, D
    while lo < hi:
        mid = (lo + hi) // 2
        if n * mid * mid >= D * D:
            hi = mid
        else:
            lo = mid + 1
    m = lo
    assert n * m * m >= D * D
    if m > 0:
        assert n * (m - 1) * (m - 1) < D * D
    return F(m, D)


worst_margin = None
worst_k = None
worst_ratio = None
for K in range(2, 64):
    U_K = up_inv_sqrt(K)
    Sbar = F(0)
    for r in range(1, K):
        U_r = up_inv_sqrt(r)
        abar = U_K + F(4, 9) * U_r
        Sbar += (K - r) * abar**3
    ratio = Sbar / K
    margin = TARGET - ratio
    assert margin > 0
    if worst_margin is None or margin < worst_margin:
        worst_margin = margin
        worst_k = K
        worst_ratio = ratio

# Independent exact check of the zeta(3/2) ingredient in the analytic K>=64 proof.
# sum_{n=1}^{16} n^{-3/2} <= sum U_n/n < 17/8 and
# sum_{n=17}^infinity n^{-3/2} <= int_{16}^infinity x^{-3/2} dx = 1/2.
zeta16_upper = sum(up_inv_sqrt(n) / n for n in range(1, 17))
assert zeta16_upper < F(17, 8)

# C27's four normalized K>=64 contributions.
analytic_envelope = F(1, 16) + F(1, 3) + F(52, 135) + F(56, 243)
assert analytic_envelope == F(19663, 19440)
assert analytic_envelope < TARGET
analytic_margin = TARGET - analytic_envelope
assert analytic_margin == F(2773, 97200)

print(f"D={D}")
print("finite_cases=62 (K=2,...,63)")
print(f"worst_K={worst_k}")
print(f"worst_ratio={worst_ratio}")
print(f"worst_ratio_float={float(worst_ratio):.15f}")
print(f"worst_margin={worst_margin}")
print(f"zeta16_upper={zeta16_upper}")
print(f"zeta16_margin={F(17,8)-zeta16_upper}")
print(f"analytic_envelope={analytic_envelope}")
print(f"target={TARGET}")
print(f"analytic_margin={analytic_margin}")
print("P24_C27_SUM756_AUDIT_PASS")
