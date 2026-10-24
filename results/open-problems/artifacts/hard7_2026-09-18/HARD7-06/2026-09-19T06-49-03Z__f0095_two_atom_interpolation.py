from fractions import Fraction
from math import comb

# HARD7-06 / F0095 exact-arithmetic certificate.
#
# We apply Ayre--Coja-Oghlan--Greenhill, Theorem 1.3 and (1.9)--(1.10),
# to q=3 and the two-atom law
#       a = p delta_x + (1-p) delta_y,
# with rational p,x,y below.  For q=3, conditioning on D and on K, the
# number of x-atoms among D iid samples, the logarithm in the first term is
# log S_{D,K}, where
#   S_{D,K}=3 A(x)^K A(y)^(D-K)-3 B(x)^K B(y)^(D-K)+x^K y^(D-K),
#   A(z)=(2+z)/3, B(z)=(1+2z)/3.
#
# Analytically, 0 < S_{D,K} <= 1 for every D,K: if each incoming message
# independently forbids no colour with probability alpha and otherwise
# forbids one uniformly random colour, S is exactly the probability that
# not all three colours have been forbidden.  Hence log S <= 0.  Therefore
# truncating the Poisson sum gives an UPPER bound on the first expectation.
#
# All transcendental quantities used for the sign are enclosed by rational
# series bounds.  Float conversions below are DISPLAY ONLY; every asserted
# sign is a Fraction comparison.

D_CERT = Fraction(46869, 10000)       # 4.6869
U_REPORTED = Fraction(4687, 1000)     # 4.687 > D_CERT
P = Fraction(117, 500)                # 0.234
X = Fraction(1911, 2500)              # 0.7644
Y = Fraction(61, 500)                 # 0.122
D_MAX = 16
LOG_TERMS = 14
EXP_TERMS = 35


def _log_core_interval(z: Fraction):
    """Rational enclosure for log(z), assuming 1/2 <= z <= 2."""
    assert Fraction(1, 2) <= z <= 2
    t = (z - 1) / (z + 1)
    t2 = t * t
    s = Fraction(0)
    power = t
    for j in range(LOG_TERMS):
        s += power / (2 * j + 1)
        power *= t2
    partial = 2 * s
    a = abs(t)
    # Tail of 2 * sum_{j>=N} t^(2j+1)/(2j+1).
    remainder = (
        2 * (a ** (2 * LOG_TERMS + 1))
        / ((2 * LOG_TERMS + 1) * (1 - t2))
    )
    return partial - remainder, partial + remainder


def log_interval(q: Fraction):
    """Rational enclosure for log(q), q>0, via power-of-two scaling."""
    assert q > 0
    z = q
    k = 0
    while z > 2:
        z /= 2
        k += 1
    while z < Fraction(1, 2):
        z *= 2
        k -= 1
    lo_z, hi_z = _log_core_interval(z)
    lo_2, hi_2 = _log_core_interval(Fraction(2))
    if k >= 0:
        return lo_z + k * lo_2, hi_z + k * hi_2
    return lo_z + k * hi_2, hi_z + k * lo_2


def exp_positive_upper(q: Fraction):
    """Rational upper bound for exp(q), q>0, from a positive Taylor tail."""
    assert q > 0
    term = Fraction(1)
    partial = Fraction(1)
    for n in range(1, EXP_TERMS + 1):
        term = term * q / n
        partial += term
    next_term = term * q / (EXP_TERMS + 1)
    ratio = q / (EXP_TERMS + 2)
    assert ratio < 1
    return partial + next_term / (1 - ratio)


def A(z):
    return (2 + z) / 3


def B(z):
    return (1 + 2 * z) / 3


def S(D, K):
    return (
        3 * (A(X) ** K) * (A(Y) ** (D - K))
        - 3 * (B(X) ** K) * (B(Y) ** (D - K))
        + (X ** K) * (Y ** (D - K))
    )


def edge_factor(a, b):
    return 1 - (1 - a) * (1 - b) / 3


# Upper-bound the truncated first expectation before the exp(-d) factor.
poisson_series_log_upper = Fraction(0)
d_power_over_fact = Fraction(1)
for D in range(D_MAX + 1):
    if D:
        d_power_over_fact = d_power_over_fact * D_CERT / D
    conditional_log_upper = Fraction(0)
    for K in range(D + 1):
        prob = Fraction(comb(D, K)) * (P ** K) * ((1 - P) ** (D - K))
        value = S(D, K)
        # Finite exact check.  The all-D fact S<=1 is also proved in the report.
        assert 0 < value <= 1
        _, log_hi = log_interval(value)
        conditional_log_upper += prob * log_hi
    poisson_series_log_upper += d_power_over_fact * conditional_log_upper

assert poisson_series_log_upper < 0

# exp(-d) >= 1 / exp_upper(d).  Since the preceding sum is negative,
# multiplying by this lower bound gives an upper bound for the first term.
exp_minus_d_lower = 1 / exp_positive_upper(D_CERT)
first_term_upper = exp_minus_d_lower * poisson_series_log_upper

# Lower-bound the edge-log expectation; subtracting it gives an upper bound.
edge_log_expect_lower = Fraction(0)
for prob, a, b in (
    (P * P, X, X),
    (2 * P * (1 - P), X, Y),
    ((1 - P) * (1 - P), Y, Y),
):
    log_lo, _ = log_interval(edge_factor(a, b))
    edge_log_expect_lower += prob * log_lo

assert edge_log_expect_lower < 0

sigma_upper = first_term_upper - D_CERT * edge_log_expect_lower / 2

print(f"d_cert = {float(D_CERT):.10f}")
print(f"reported_endpoint = {float(U_REPORTED):.10f}")
print(f"p = {float(P):.10f}")
print(f"x = {float(X):.10f}")
print(f"y = {float(Y):.10f}")
print(f"D_max = {D_MAX}")
print(f"first_term_upper ~= {float(first_term_upper):.18e}")
print(f"edge_log_expect_lower ~= {float(edge_log_expect_lower):.18e}")
print(f"Sigma_upper ~= {float(sigma_upper):.18e}")
print(f"SIGMA_STRICTLY_NEGATIVE = {sigma_upper < 0}")
print(f"D_CERT_STRICTLY_BELOW_REPORTED_ENDPOINT = {D_CERT < U_REPORTED}")
print(
    "ACG implication: d_3^* <= d_cert < 4.687, so Theorem 1.3 gives "
    "chi(G(n,4.687/n)) > 3 w.h.p."
)
print(
    "ALL_EXACT_CHECKS_PASS = "
    f"{(sigma_upper < 0) and (D_CERT < U_REPORTED)}"
)
