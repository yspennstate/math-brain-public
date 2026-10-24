from fractions import Fraction

A8 = Fraction(
    4688722489067361283750127182134186345695457354381617699,
    7437921710332085596529852377779940412620800000000000000,
)
A0 = Fraction(
    127596793342690034600361684870097,
    197703921604834678505472000000000,
)
C0 = Fraction(27865448, 206955)
BETA0 = Fraction(
    713425217726611388616507115106921327,
    740604339057582092285156250000000000,
)
C1 = Fraction(26633487052538711, 2329665975000)
CONE_OLD = Fraction(2, 3)
CONE_NEW = Fraction(63039, 100000)

g2 = CONE_OLD - A8
g1814 = CONE_NEW - A8
eta2 = g2 / A8
eta1814 = g1814 / A8

# New asymmetric pair u=(10,21), v=(10,-20), u+v=(20,1).
kappa = 20 * CONE_OLD - 21 * A8
old_kappa = 20 * CONE_OLD - 21 * A0

# Finite residual lower bound at scale n=32.
n = 32
finite_error = CONE_OLD * C0 * (20 * BETA0 ** (10 * n))
finite_margin = kappa - finite_error

# Axis-Busemann residual in the old slope-2 cone: m=a n=209 suffices.
m2 = 209
buse_steep = g2 - CONE_OLD * C0 * (BETA0 ** m2)

# Axis-Busemann residual in the new slope-907/500 cone at m=a n=90000.
# beta_hat = 12497/12500 = 1-3/12500, hence beta_hat^m <= exp(-3m/12500).
# Certify exp(t) from below by the degree-30 Taylor polynomial, all exactly rational.
m1 = 90000
t = Fraction(3 * m1, 12500)
S = Fraction(1, 1)
term = Fraction(1, 1)
for k in range(1, 31):
    term = term * t / k
    S += term
buse_shallow_cert = g1814 - CONE_NEW * C1 / S

checks = {
    "g2_positive": g2 > 0,
    "g1814_positive": g1814 > 0,
    "pair_kappa_positive": kappa > 0,
    "previous_pair_bound_nonpositive": old_kappa <= 0,
    "n32_margin_positive": finite_margin > 0,
    "steep_m209_margin_positive": buse_steep > 0,
    "shallow_m90000_cert_margin_positive": buse_shallow_cert > 0,
}

print("P20-T10-BUSEMANN-CONE-CHECK")
print("A8_exact =", A8)
print("A8_float =", f"{float(A8):.15f}")
print("g2_exact =", g2)
print("g2_float =", f"{float(g2):.15f}")
print("eta2_float =", f"{float(eta2):.15f}")
print("g1814_exact =", g1814)
print("g1814_float =", f"{float(g1814):.15e}")
print("eta1814_float =", f"{float(eta1814):.15e}")
print("pair_kappa_exact =", kappa)
print("pair_kappa_float =", f"{float(kappa):.15f}")
print("previous_A0_pair_bound_float =", f"{float(old_kappa):.15f}")
print("n32_error_float =", f"{float(finite_error):.15f}")
print("n32_margin_float =", f"{float(finite_margin):.15f}")
print("n32_total_expected_residual_lower_float =", f"{float(n * finite_margin):.15f}")
print("steep_m209_margin_float =", f"{float(buse_steep):.15e}")
print("shallow_taylor_t =", t)
print("shallow_m90000_cert_margin_float =", f"{float(buse_shallow_cert):.15e}")
for name, ok in checks.items():
    print(name, "=", ok)
assert all(checks.values())
print("ALL_EXACT_CHECKS_PASS")
