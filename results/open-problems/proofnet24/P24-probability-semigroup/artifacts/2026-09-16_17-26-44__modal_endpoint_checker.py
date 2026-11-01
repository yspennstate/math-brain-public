from fractions import Fraction as F

# Exact-arithmetic self-check for P24-AV-P3-SINGLEMODE-ENDPOINT-54.
# kappa_p is the homogeneous Ito dissipation after time/frequency scaling.

def kappa(p):
    return p * (F(3) - p) / F(2)


def gamma(p):
    return p * (p - F(3)) / F(2)


for p in [F(2), F(9, 4), F(5, 2), F(8, 3), F(11, 4), F(29, 10)]:
    k = kappa(p)
    assert k > 0
    assert gamma(p) == -k

    # In the written Ito proof, the three mixed/input terms have coefficients
    # p, p(p-1), p(p-1)/2.  These epsilons spend exactly kappa/6 each,
    # leaving kappa/2 of the homogeneous dissipation.
    eps_f = k / (F(6) * p)
    eps_cross = k / (F(6) * p * (p - F(1)))
    eps_quad = k / (F(3) * p * (p - F(1)))
    spent = p * eps_f + p * (p - F(1)) * eps_cross + p * (p - F(1)) / F(2) * eps_quad
    assert spent == k / F(2)
    print(f"p={p}: kappa={k}, gamma={gamma(p)}, retained_dissipation={k/F(2)}")

assert kappa(F(3)) == 0
assert gamma(F(3)) == 0
assert gamma(F(4)) == F(2)
assert gamma(F(2)) == F(-1)

# General beta family retained from the previous report.
for R in [F(5, 2), F(3), F(4), F(10)]:
    beta2 = F(1) + F(1) / (R - F(1))
    rc = F(1) + F(2) / beta2
    assert beta2 < F(2)
    assert rc == F(3) - F(2) / R
    assert rc < R
    print(f"R={R}: beta^2={beta2}, r_c={rc}<R")

print("P24_AV_P3_MODAL_ENDPOINT_EXACT_CHECK_PASS")
