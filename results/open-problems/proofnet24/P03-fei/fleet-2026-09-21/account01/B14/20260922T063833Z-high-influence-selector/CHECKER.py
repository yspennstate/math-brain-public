from fractions import Fraction
from math import isqrt

# Exact-decimal live center.
C = Fraction(3260925607, 500000000)  # 6.521851214
D0 = Fraction(1741, 10000)


def ln_ge1_bounds(x, terms=180):
    """Rigorous rational bounds for ln(x), x>=1, via the positive atanh series."""
    assert x >= 1
    if x == 1:
        return Fraction(0), Fraction(0)
    z = (x - 1) / (x + 1)
    z2 = z * z
    term = z
    s = Fraction(0)
    for k in range(terms):
        s += term / (2 * k + 1)
        term *= z2
    lo = 2 * s
    # Positive remaining series:
    # sum_{k>=N} z^(2k+1)/(2k+1)
    # <= z^(2N+1)/((2N+1)(1-z^2)).
    hi = lo + 2 * term / ((2 * terms + 1) * (1 - z2))
    return lo, hi


LN2_LO, LN2_HI = ln_ge1_bounds(Fraction(2))


def h2_bounds(x, terms=180):
    """Rigorous rational bounds for binary entropy h_2(x), rational x."""
    assert 0 <= x <= 1
    if x == 0 or x == 1:
        return Fraction(0), Fraction(0)
    ax_lo, ax_hi = ln_ge1_bounds(1 / x, terms)
    bx_lo, bx_hi = ln_ge1_bounds(1 / (1 - x), terms)
    num_lo = x * ax_lo + (1 - x) * bx_lo
    num_hi = x * ax_hi + (1 - x) * bx_hi
    return num_lo / LN2_HI, num_hi / LN2_LO


def sqrt_bounds(r, digits=120):
    """Rational [lo,hi] containing sqrt(r)."""
    assert r >= 0
    Q = 10 ** digits
    n = isqrt((r.numerator * Q * Q) // r.denominator)
    lo, hi = Fraction(n, Q), Fraction(n + 1, Q)
    assert lo * lo <= r < hi * hi
    return lo, hi


# At d0, Psi(|1-2d|)=h_2(1/2-sqrt(d(1-d))).
s_lo, s_hi = sqrt_bounds(D0 * (1 - D0))
y_lo = Fraction(1, 2) - s_hi
y_hi = Fraction(1, 2) - s_lo
assert 0 < y_lo <= y_hi < Fraction(1, 2)

phi_lo, phi_hi = h2_bounds(y_lo)
hd_lo, hd_hi = h2_bounds(D0)

F_LO = C * D0 - 1 - hd_hi + phi_lo

# For d in [d0,1/2],
# F'(d) >= C - log_2((1-d0)/d0) - 2/ln 2.
ratio = (1 - D0) / D0
lr_lo, lr_hi = ln_ge1_bounds(ratio)
LOGRATIO_HI = lr_hi / LN2_LO
TWO_OVER_LN2_HI = Fraction(2) / LN2_LO
DERIV_LO = C - LOGRATIO_HI - TWO_OVER_LN2_HI

assert F_LO > 0
assert DERIV_LO > 0
assert C / Fraction(2) - 2 > 0  # F(1/2)>0.


def dec(q, digits=18):
    # Decimal display only; all theorem comparisons use exact Fractions above.
    sign = "-" if q < 0 else ""
    q = abs(q)
    scale = 10 ** digits
    n = (q.numerator * scale) // q.denominator
    return f"{sign}{n // scale}.{n % scale:0{digits}d}"


print("PASS")
print("d0 =", f"{D0.numerator}/{D0.denominator}", "=", dec(D0, 10))
print("certified F(d0) lower >", dec(F_LO, 18))
print("certified derivative lower on [d0,1/2] >", dec(DERIV_LO, 18))
print("certified F(1/2) =", dec(C / Fraction(2) - 2, 18), "> 0")
print("ln2 enclosure width <", dec(LN2_HI - LN2_LO, 60))
