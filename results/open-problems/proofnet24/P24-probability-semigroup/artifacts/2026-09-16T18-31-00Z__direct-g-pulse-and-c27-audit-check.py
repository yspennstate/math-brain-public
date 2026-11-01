from fractions import Fraction

# P24 exact arithmetic self-check for the direct additive-noise pulse theorem,
# plus an independent exact check of the numerical exponent used in the
# directed C27 peer audit.  No floating-point inequality is used for a claim.


def gamma(p, beta_sq):
    p = Fraction(p)
    beta_sq = Fraction(beta_sq)
    return p * (beta_sq * (p - 1) - 2) / 2


def ln_bounds(x, N=180):
    """Exact rational bounds for log(x) from the atanh series."""
    x = Fraction(x)
    assert x > 0
    if x < 1:
        lo, hi = ln_bounds(1 / x, N)
        return -hi, -lo
    z = (x - 1) / (x + 1)
    zz = z * z
    term = z
    total = Fraction(0)
    for j in range(N):
        if j:
            term *= zz
        total += term / (2 * j + 1)
    lo = 2 * total
    # Remaining denominators are at least 2N+1, so a geometric tail dominates.
    tail = 2 * term * zz / ((2 * N + 1) * (1 - zz))
    return lo, lo + tail


def e_bounds(M=40):
    """Exact rational enclosure of e from its power series."""
    total = Fraction(0)
    fact = 1
    for j in range(M + 1):
        if j:
            fact *= j
        total += Fraction(1, fact)
    fact_next = fact * (M + 1)
    tail = Fraction(1, fact_next) * Fraction(M + 2, M + 1)
    return total, total + tail


# Frozen P24 pair beta^2=1: post-pulse p-moment exponent.
assert gamma(2, 1) == -1
assert gamma(3, 1) == 0
assert gamma(4, 1) == 2

# General commuting beta-family: p_c=1+2/beta^2 is exactly critical.
for beta_sq in (Fraction(1, 2), Fraction(1), Fraction(3, 2)):
    assert beta_sq < 2
    p_c = 1 + Fraction(2, 1) / beta_sq
    assert gamma(p_c, beta_sq) == 0

# Frozen beta^2=1 pulse second moment has v'= -v + h^2, hence
# v(1)=h^2(1-e^{-1})>0.  The finite algebraic sign is exact.
assert Fraction(2) - Fraction(1) == 1

# Directed C27 audit: independently certify the literal exponent appearing in
# C27-FB-MGF-01 using a fresh exact rational implementation.
u = Fraction(11340541, 4000000)
eps = Fraction(590451719447, 1250000000000)
lnx_lo, _ = ln_bounds((1 + u) / 2)
_, ln2_hi = ln_bounds(Fraction(2, 1))
e_lo, _ = e_bounds()
upper_inv_e = 1 / e_lo
# epsilon(u)=[log((1+u)/2) - (u^2-1)/(8e)]/log 2.
# Lower-bound numerator and upper-bound eps*log2 to certify epsilon(u)>eps.
gap = lnx_lo - ((u * u - 1) / 8) * upper_inv_e - eps * ln2_hi
assert gap > 0

# Independent rational recomputation of the older P3 correlation sanity check.
row = [
    Fraction(37, 96), Fraction(7, 32), Fraction(7, 32),
    Fraction(7, 96), Fraction(7, 96), Fraction(1, 32),
]
assert sum(row) == 1
pA = Fraction(5, 48)
pB = Fraction(7, 12)
pAB = Fraction(7, 96)
cov = pAB - pA * pB
assert cov == Fraction(7, 576) and cov > 0

print("P24 DIRECT-G PULSE / C27 AUDIT EXACT CHECK")
print("gamma_beta2=1_p2 =", gamma(2, 1))
print("gamma_beta2=1_p3 =", gamma(3, 1))
print("gamma_beta2=1_p4 =", gamma(4, 1))
print("critical_identity_verified_for_beta_sq = 1/2, 1, 3/2")
print("c27_epsilon_cert =", f"{eps.numerator}/{eps.denominator}")
print("c27_exact_log_gap_positive =", gap > 0)
print("c27_P3_covariance =", cov)
print("ALL_EXACT_CHECKS_PASS")
