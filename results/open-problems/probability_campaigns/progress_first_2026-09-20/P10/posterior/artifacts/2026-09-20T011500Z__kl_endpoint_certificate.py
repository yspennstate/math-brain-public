from fractions import Fraction

# Exact-arithmetic certificate for the binary-tree q=3 Potts KL Lyapunov.
# It proves:
#   (i) lambda_lo = 0.70237785 still has eta_3(lambda_lo) < 1/2;
#   (ii) lambda_hi = 0.70237786 already fails the plain KL inequality,
#        at the explicit rational posterior x = 0.5283699 in the one-large-
#        coordinate reduction.
# Thus the endpoint of this particular plain-KL method lies in
# [0.70237785, 0.70237786).
#
# All logarithms are enclosed with rational atanh-series bounds.

LAM_LO = Fraction(14047557, 20000000)   # 0.70237785
LAM_HI = Fraction(35118893, 50000000)   # 0.70237786
THIRD = Fraction(1, 3)
ONE = Fraction(1, 1)
NTERMS = 280


def ln_bounds(x: Fraction, n: int = NTERMS):
    assert x > 0
    if x == 1:
        return Fraction(0), Fraction(0)
    if x < 1:
        lo, hi = ln_bounds(1 / x, n)
        return -hi, -lo
    t = (x - 1) / (x + 1)
    t2 = t * t
    s = Fraction(0)
    power = t
    for k in range(n):
        s += power / (2 * k + 1)
        power *= t2
    s *= 2
    rem = 2 * power / ((2 * n + 1) * (1 - t2))
    return s, s + rem


def mul_ln_bounds(c: Fraction, x: Fraction):
    assert c >= 0 and x > 0
    if c == 0:
        return Fraction(0), Fraction(0)
    lo, hi = ln_bounds(x)
    return c * lo, c * hi


def d_bounds(x: Fraction):
    # d(x)=x log(3x)+(1-x)log(3(1-x)/2), 0 log 0 := 0.
    if x == 0:
        a = (Fraction(0), Fraction(0))
    else:
        a = mul_ln_bounds(x, 3 * x)
    y = 1 - x
    if y == 0:
        b = (Fraction(0), Fraction(0))
    else:
        b = mul_ln_bounds(y, Fraction(3, 2) * y)
    return a[0] + b[0], a[1] + b[1]


def affine(x: Fraction, lam: Fraction):
    return THIRD + lam * (x - THIRD)


def g_bounds(x: Fraction, lam: Fraction):
    # G_lambda(x)=d(x)-2d(1/3+lambda(x-1/3)).
    dlo, dhi = d_bounds(x)
    elo, ehi = d_bounds(affine(x, lam))
    return dlo - 2 * ehi, dhi - 2 * elo


def dprime_bounds(x: Fraction):
    return ln_bounds(2 * x / (1 - x))


def gprime_bounds(x: Fraction, lam: Fraction):
    lo1, hi1 = dprime_bounds(x)
    lo2, hi2 = dprime_bounds(affine(x, lam))
    return lo1 - 2 * lam * hi2, hi1 - 2 * lam * lo2


def q_second_numerator(x: Fraction, lam: Fraction):
    # sign(G''_lambda) = sign(Q_lambda) on (1/3,1).
    return (
        lam * lam * x * x
        + lam * (1 - 4 * lam) * x / 3
        + (2 - lam - lam * lam) / 9
    )


# ---- Lower endpoint: certify global positivity of G. ----
# Q is upward-opening. These signs force one root in (1/3,0.4),
# one in (0.4,0.49), and therefore G''>0 on [0.49,1].
assert q_second_numerator(THIRD, LAM_LO) > 0
assert q_second_numerator(Fraction(2, 5), LAM_LO) < 0
assert q_second_numerator(Fraction(49, 100), LAM_LO) > 0

# By G(1/3)=G'(1/3)=0 and the Q-sign pattern, G first rises, then its
# derivative falls. This exact sign shows that by x=.49 the derivative is
# negative, so the pre-.49 stationary point is a local maximum.
assert gprime_bounds(Fraction(49, 100), LAM_LO)[1] < 0

# The unique post-.49 stationary point is bracketed here.
L = Fraction(52836946, 100000000)
U = Fraction(52836947, 100000000)
gpL = gprime_bounds(L, LAM_LO)
gpU = gprime_bounds(U, LAM_LO)
assert gpL[1] < 0
assert gpU[0] > 0

# Since G''>0 throughout this bracket, |G'| is maximized at an endpoint.
# The following exact Lipschitz enclosure proves the local minimum is >0.
gL = g_bounds(L, LAM_LO)
M = max(-gpL[0], gpU[1])
min_lower = gL[0] - M * (U - L)
assert min_lower > 0

# The terminal endpoint is also strictly positive. Together with the
# derivative-shape argument above this certifies G>0 on (1/3,1].
g1 = g_bounds(ONE, LAM_LO)
assert g1[0] > 0

# ---- Upper endpoint: explicit failure witness for the plain KL method. ----
XW = Fraction(5283699, 10000000)
gw = g_bounds(XW, LAM_HI)
assert gw[1] < 0

print("PASS")
print("lambda_lo =", float(LAM_LO))
print("lambda_hi =", float(LAM_HI))
print("Q_lo(1/3), Q_lo(0.4), Q_lo(0.49) =",
      *(float(q_second_numerator(x, LAM_LO))
        for x in (THIRD, Fraction(2, 5), Fraction(49, 100))))
print("G'_lo(0.49) upper =", float(gprime_bounds(Fraction(49,100), LAM_LO)[1]))
print("G'_lo(L) upper =", float(gpL[1]))
print("G'_lo(U) lower =", float(gpU[0]))
print("certified G_lo(local minimum) lower >", float(min_lower))
print("G_lo(1) lower =", float(g1[0]))
print("failure witness x =", float(XW))
print("G_hi(x) upper <", float(gw[1]))
