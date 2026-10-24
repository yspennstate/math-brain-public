#!/usr/bin/env python3
"""
Exact rational certificate for R18 / I0080 explicit small-time witness.

No floating-point computation is used for any certified inequality.

Constants:
  p = 3/50,
  ell = 19,
  D = 4573/100000,
  b0 = 1/320,
  epsilon = 1/1600.

For 0<b<=b0 the run report proves analytically that, after removing the common
factor A_b=pi/(pi-b), the exact finite-b kernel differs from its b->0 Cauchy
kernel by <epsilon uniformly on |v|<=19.

This checker certifies:
  (i) the exact rational kernel-error inequalities used in that proof;
  (ii) exact rational enclosures of pi via Machin's formula;
  (iii) exact alternating-series enclosures of the three limiting Cauchy
       witness values Q(1/2), Q(2), Q(35/4);
  (iv) the strict margins Q(1/2)>D+epsilon,
       Q(2)<D-epsilon,
       Q(35/4)>D+epsilon;
  (v) a rigorous rational enclosure for
       T*=b0^2/(pi D)=125/(585344*pi).
"""
from fractions import Fraction as F


def atan_alt_bounds(z, n):
    """Exact enclosure of atan(z), 0<=z<=1, from n-term alternating series."""
    assert F(0) <= z <= F(1)
    s = F(0)
    for k in range(n):
        s += (-1) ** k * z ** (2 * k + 1) / F(2 * k + 1)
    nxt = z ** (2 * n + 1) / F(2 * n + 1)
    if n % 2 == 0:
        return s, s + nxt
    return s - nxt, s


# Machin: pi = 16 atan(1/5) - 4 atan(1/239).
a5_lo, a5_hi = atan_alt_bounds(F(1, 5), 24)
a239_lo, a239_hi = atan_alt_bounds(F(1, 239), 8)
PI_LO = 16 * a5_lo - 4 * a239_hi
PI_HI = 16 * a5_hi - 4 * a239_lo
assert PI_LO < PI_HI
assert PI_LO > F(333, 106)
assert PI_HI < F(355, 113)
print("pi enclosure:")
print("  lower =", PI_LO)
print("  upper =", PI_HI)
print("  width =", PI_HI - PI_LO)

# Kernel-error rational bounds for b<=1/320 and |v|<=19.
bden = 320
B_LO = F(1) - F(1, 6 * bden * bden)  # sin(b)/b >= 1-b^2/6
# cosh(x) <= 1/(1-x^2/2), |x|<=19/320; hence C >= 1/cosh_bound.
C_LO = F(2 * bden * bden - 19 * 19, 2 * bden * bden)
# Lower denominator bound gives C <= 1/(1-b^2/12).
C_HI = F(12 * bden * bden, 12 * bden * bden - 1)
REL_LOSS = F(1) - B_LO * C_LO
REL_GAIN = C_HI - F(1)
assert REL_LOSS < F(3, 1600)
assert REL_GAIN < F(3, 1600)
# Since P0(v)=1/[pi(1+v^2)] < 1/3, absolute error < 1/1600.
print("normalized-kernel relative loss upper =", REL_LOSS)
print("normalized-kernel relative gain upper =", REL_GAIN)
print("both < 3/1600: PASS")

p = F(3, 50)
ell = F(19)
D = F(4573, 100000)
eps = F(1, 1600)


def delta_bounds(y):
    """Bounds for atan(y)-atan(y-19) at the three rational sample points."""
    if y == F(1, 2):
        a_lo, a_hi = atan_alt_bounds(F(1, 2), 50)
        b_lo, b_hi = atan_alt_bounds(F(2, 37), 30)
        return a_lo + PI_LO / 2 - b_hi, a_hi + PI_HI / 2 - b_lo
    if y == F(2):
        a_lo, a_hi = atan_alt_bounds(F(1, 2), 50)
        b_lo, b_hi = atan_alt_bounds(F(1, 17), 30)
        return PI_LO - a_hi - b_hi, PI_HI - a_lo - b_lo
    if y == F(35, 4):
        a_lo, a_hi = atan_alt_bounds(F(4, 35), 30)
        b_lo, b_hi = atan_alt_bounds(F(4, 41), 30)
        return PI_LO - a_hi - b_hi, PI_HI - a_lo - b_lo
    raise ValueError(y)


def Q_bounds(y):
    # Q(y)=p/[pi(1+y^2)]+(1-p)/(ell*pi)*(atan(y)-atan(y-ell)).
    dlo, dhi = delta_bounds(y)
    const = p / (F(1) + y * y)
    nlo = const + (F(1) - p) / ell * dlo
    nhi = const + (F(1) - p) / ell * dhi
    return nlo / PI_HI, nhi / PI_LO


samples = [F(1, 2), F(2), F(35, 4)]
for y in samples:
    lo, hi = Q_bounds(y)
    print("Q", y, "in [", lo, ",", hi, "]")
    if y == F(2):
        assert hi < D - eps
        print("  certified Q(2) < D-epsilon")
    else:
        assert lo > D + eps
        print("  certified Q(y) > D+epsilon")
print("three limiting witness inequalities: PASS")

# T*=b0^2/(pi D)=125/(585344*pi).
b0 = F(1, 320)
T_LO = b0 * b0 / (PI_HI * D)
T_HI = b0 * b0 / (PI_LO * D)
assert T_LO < T_HI
assert T_LO > F(67, 1_000_000)
assert T_HI < F(69, 1_000_000)
print("T* exact form = 125/(585344*pi)")
print("T* rational enclosure = [", T_LO, ",", T_HI, "]")
print("certified 0.000067 < T* < 0.000069")
print("PASS")
